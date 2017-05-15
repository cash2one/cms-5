#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Tom
# date: 2016-01-18
# description: 金融频道服务接口

import logging
import json
import requests

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404

from cbbweb.cms import models as cmsmodels
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils import (str2array, to_dict, get_method_dict, convert_obj)
from cbbweb.core.utils import db
from django.conf import settings
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import (get_object, list_objs)
from cbbweb.service.cms_utils.common_utils import (to_float, to_int)
from cbbweb.service.cms_utils import offer_price_utils

logger = logging.getLogger('service')

'''
后期优化建议：
    1. 数据不要放在数据库中计算
    2. 合并不必要拆分的表
'''


@redis_func()
def get_lowest_monthly_payment(city_id=None, car_series_id=None,
                               car_type_id=None, dealer_id=None,
                               finacial_product_id=None, price=None):
    '''
        根据城市、车系，获取最低月供的金融方案
    '''
    offer_price  = {
        "public_offer_price": price,
        "car_series_id": car_series_id,
        "car_type_id": car_type_id,
        "dealer_id": dealer_id
    }
    if not price:
        kw = {}
        if car_series_id: kw['car_series_id'] = car_series_id
        if car_type_id: kw['car_type_id'] = car_type_id
        if dealer_id: kw['dealer_id'] = dealer_id
        _offer_price = offer_price_utils.get_offerprice(**kw)
        offer_price['public_offer_price'] = _offer_price['public_offer_price']

    sql = """
        select * from (
            select
            p.id as product_id,
            p.is_final_payment,
            p.final_payment_scale,
            p.repayment_type,
            fpp.id as first_percent_id,
            fpp.FIRST_PAY_PERCENT as first_pay_percent,
            sku.id as sku_id,
            sku.SKU_ITEM as sku_item,
            sku.sku_rate as sku_rate,
            first_pay_percent * sku_item as less_monthly_flag
            FROM
            t_base_financial_product p,
            t_base_financial_first_pay_percent_rel fpp,
            t_base_financial_pro_sku sku,
            t_base_financial_series_rel fs
            where
            p.id = fpp.FINACIAL_PRODUCT_ID and
            p.id = sku.FINACIAL_PRODUCT_ID and
            p.id = fs.FINANCIAL_PRODUCT_ID and
            p.EFFECT_START_DATE <= now() and
            p.EFFECT_END_DATE >= now() and
            p.is_enable = 1 and
            fs.CAR_SERIES_ID = %(car_series_id)s
            {% if finacial_product_id -%}
            and p.id = %(finacial_product_id)s
            {%- endif %}
        ) xxx
        order by xxx.less_monthly_flag desc
        limit 1;
    """

    kw = {'car_series_id':car_series_id,
          'finacial_product_id': finacial_product_id}
    finance_data = db.fetchone(sql, kw)
    if not finance_data:
        return {}

    finance_data.update(offer_price)

    rtn_data = calc_financial(**finance_data)
    finance_data.update(rtn_data)

    return finance_data


@redis_func()
def get_financial_pack_data(city_id=None, car_series_id=None, car_type_id=None,
                            dealer_id=None, finacial_product_id=None,
                            sku_item=None, first_pay_percent=None):
    '''
        根据参数，获取金融相关包装数据
    '''
    finance_data = get_object(model=ModelName.T_BASE_FINANCIAL_PRODUCT,
                              id=finacial_product_id, is_enable=1)
    finance_data = convert_obj(finance_data)

    # fetch finance corp
    finance_corp = get_object(model=ModelName.T_BASE_FINANCIAL_CORP,
                              id=finance_data['financial_corp_id'], is_enable=1)
    finance_data['corp_id'] = finance_corp.id
    finance_data['corp_name'] = finance_corp.corp_name

    # fetch price
    kw = {}
    if car_series_id: kw['car_series_id'] = car_series_id
    if car_type_id: kw['car_type_id'] = car_type_id
    if dealer_id: kw['dealer_id'] = dealer_id
    _offer_price = offer_price_utils.get_offerprice(**kw)
    offer_price = {
        "public_offer_price": _offer_price['public_offer_price'],
        "car_series_id": car_series_id,
        "car_type_id": car_type_id,
        "dealer_id": dealer_id
    }
    finance_data.update(offer_price)

    # fetch first pay percent
    first_pay_percent_obj = get_object(
        model=ModelName.T_BASE_FINANCIAL_FIRST_PAY_PERCENT_REL,
        finacial_product_id=finacial_product_id,
        first_pay_percent=first_pay_percent, is_enable=1)
    if not first_pay_percent_obj:
        return {}
    first_pay_percent_obj = convert_obj(first_pay_percent_obj)
    finance_data['first_pay_percent_id'] = first_pay_percent_obj['id']
    finance_data['first_pay_percent'] = first_pay_percent_obj['first_pay_percent']

    # fetch sku
    financial_pro_sku_obj = get_object(
        model=ModelName.T_BASE_FINANCIAL_PRO_SKU, is_enable=1,
        finacial_product_id=finacial_product_id, sku_item=sku_item)
    if not financial_pro_sku_obj:
        return {}

    financial_pro_sku_obj = convert_obj(financial_pro_sku_obj)
    finance_data['sku_id'] = financial_pro_sku_obj['id']
    finance_data['sku_name'] = financial_pro_sku_obj['sku_name']
    finance_data['sku_item'] = financial_pro_sku_obj['sku_item']
    finance_data['sku_rate'] = financial_pro_sku_obj['sku_rate']

    rtn_data = calc_financial(**finance_data)
    finance_data.update(rtn_data)

    return finance_data


@redis_func()
def list_financials(car_series_id=None, car_type_id=None, dealer_id=None,
                    first_pay_percent=0, sku_item=0, city_id=None,
                    order_by='monthly_payment', corp_ids=None):
    '''
    '''
    order_dict = {
        'monthly_payment':'xxx.less_monthly_flag',
        '-monthly_payment':'xxx.less_monthly_flag desc',
        'hot':'xxx.pass_percent',
        '-hot':'xxx.pass_percent desc',
    }
    sql = """
        select distinct * from (
            select
            c.id as corp_id,
            c.corp_name,
            c.corp_logo,
            p.id as product_id,
            p.financial_product_name,
            p.pass_percent,
            p.repayment_type,
            p.is_final_payment,
            p.final_payment_scale,
            fpp.id as first_percent_id,
            fpp.FIRST_PAY_PERCENT as first_pay_percent,
            sku.id as sku_id,
            sku.SKU_ITEM as sku_item,
            sku.sku_rate as sku_rate,
            first_pay_percent * sku_item as less_monthly_flag
            FROM
            t_base_financial_product p,
            t_base_financial_corp c,
            t_base_financial_first_pay_percent_rel fpp,
            t_base_financial_pro_sku sku,
            t_base_financial_series_rel fs
            where
            p.id = fpp.FINACIAL_PRODUCT_ID and
            p.FINANCIAL_CORP_ID=c.ID and
            p.id = sku.FINACIAL_PRODUCT_ID and
            p.id = fs.FINANCIAL_PRODUCT_ID and
            p.EFFECT_START_DATE <= now() and
            p.EFFECT_END_DATE >= now() and
            p.is_enable = 1 and
            fs.CAR_SERIES_ID = %(car_series_id)s and
            fpp.FIRST_PAY_PERCENT = %(first_pay_percent)s and
            sku.sku_item = %(sku_item)s
            {% if corp_ids %}
            and c.id in ({{corp_ids}})
            {% endif %}
        ) xxx
        {% if order_by -%}
        order by {{order_by}}
        {% endif %}
    """

    kw = {}
    kw['car_series_id'] = car_series_id
    kw['first_pay_percent'] = first_pay_percent
    kw['sku_item'] = sku_item
    kw['corp_ids'] = corp_ids
    kw['order_by'] = order_dict.get(order_by, None)
    finance_datas = db.fetch(sql, kw)

    kw = {}
    if car_series_id: kw['car_series_id'] = car_series_id
    if car_type_id: kw['car_type_id'] = car_type_id
    if dealer_id: kw['dealer_id'] = dealer_id
    offer_price = offer_price_utils.get_offerprice(**kw)


    for finance_data in finance_datas:
        finance_data['public_offer_price'] = offer_price['public_offer_price']
        rtn_data = calc_financial(**finance_data)
        finance_data.update(rtn_data)


    for item in finance_datas:
        sql = "SELECT condition_name FROM t_base_financial_condition_rel WHERE is_enable=1 and FINACIAL_PRODUCT_ID = " + str(item['product_id']) + " GROUP BY CONDITION_NAME"
        item['conditions'] = db.fetch_col_array(sql,{},'condition_name')
        sql = "SELECT material_name FROM t_base_financial_material_rel WHERE is_enable=1 and FINACIAL_PRODUCT_ID = " + str(item['product_id']) + " GROUP BY MATERIAL_NAME"
        item['materials'] = db.fetch_col_array(sql,{},'material_name')
        sql = """
            select
            b.dict_key,b.dict_value,b.dict_ext_values,
            a.id,a.FEATURE_ID
            from t_base_financial_feature_rel a, t_base_data_dict b
            where
            b.id = a.feature_id and
            a.IS_ENABLE = 1 and
            b.is_enable = 1 and
            FINACIAL_PRODUCT_ID=%(product_id)s
        """
        features = db.fetch(sql, {'product_id':item['product_id']})
        for feature in features:
            feature['dict_ext_values'] = eval(feature['dict_ext_values'])
        item['features'] = features

    # order by monthly pay amount
    if 'monthly_payment' in order_by :
        reverse_flag = True if '-' in order_by else False
        finance_datas = sorted(finance_datas, reverse=reverse_flag,
                               key=lambda t: t['monthly_pay_amount'])

    return finance_datas


def calc_financial(**kwargs):
    '''
        @args:
        first_pay_percent   首付比例
        sku_item            期数
        sku_rate            年利率
        public_offer_price  价格
        is_final_payment    是否尾款产品
        final_payment_scale 尾款比例
        repayment_type      还款方式

        @return
        first_pay_amount    首付
        loan_amount         贷款金额
        monthly_pay_amount  月供
        loan_cost           成本
        final_payment_amount尾款
    '''
    first_pay_percent = to_float(kwargs['first_pay_percent'])
    sku_item = to_float(kwargs['sku_item'])
    public_offer_price = to_float(kwargs['public_offer_price'])
    is_final_payment = to_int(kwargs['is_final_payment'])
    repayment_type = kwargs['repayment_type']
    final_payment_scale = to_float(kwargs.get('final_payment_scale', 0.0))
    sku_rate = kwargs['sku_rate']

    # calc downpay
    first_pay_amount = round( public_offer_price * first_pay_percent / 100, 2)
    kwargs['first_pay_amount'] = first_pay_amount
    # calc loan
    loan_amount = public_offer_price - first_pay_amount
    kwargs['loan_amount'] = loan_amount
    # calc monthly pay amount


    final_payment_amount = 0
    if kwargs['is_final_payment'] == 1:
        final_payment_amount = public_offer_price * final_payment_scale /100

    # calc monthly pay amount
    interest_rtn = interest_calc(interest_method=repayment_type,
                                 loan_amount=loan_amount, interest_rate=sku_rate,
                                 sku_item=sku_item,
                                 final_payment_amount=final_payment_amount)
    kwargs['monthly_pay_amount'] = interest_rtn['monthly_payment']

    kwargs['loan_cost'] = interest_rtn['interest_amount']
    kwargs['final_payment_amount'] = final_payment_amount

    return kwargs


def interest_calc(interest_method=None, loan_amount=None, interest_rate=None,
                  sku_item=None, final_payment_amount=0):
    PAYMENT_METHOD = {
        'CREDIT': 'paymentMethod1857', #信用卡分期
        'CREDIT_NO_INTEREST': 'paymentMethod1860', #'信用卡分期（不含利息）',
        'EQ_AMOUNT': 'paymentMethod2601', #'等额本息',
        '100LOAN': 'paymentMethod2628' #'百禄贷'
    }
    loan_amount = float(loan_amount)
    monthly_interest_rate = float(interest_rate)/12/100
    sku_item = float(sku_item)
    final_payment_amount = float(final_payment_amount)

    if monthly_interest_rate == 0 :
        return {
            "monthly_payment": round(loan_amount/sku_item,2),
            "interest_amount": 0,
        }
    if PAYMENT_METHOD['CREDIT'] == interest_method:
        interest_amount = loan_amount * float(interest_rate)/100
        monthly_payment = (loan_amount+interest_amount)/sku_item

        return {
            "monthly_payment": round(monthly_payment,2),
            "interest_amount": round(interest_amount,2),
        }
    elif PAYMENT_METHOD['CREDIT_NO_INTEREST'] == interest_method:
        interest_amount = loan_amount * float(interest_rate)/100
        monthly_payment = loan_amount/sku_item
        return {
            "monthly_payment": round(monthly_payment,2),
            "interest_amount": round(interest_amount,2),
        }
    elif PAYMENT_METHOD['EQ_AMOUNT'] == interest_method:
        monthly_payment = 0
        interest_amount = 0
        if monthly_interest_rate != 0:
            monthly_payment = ( loan_amount * monthly_interest_rate * (1+monthly_interest_rate) ** sku_item ) / ((1 + monthly_interest_rate) ** sku_item - 1)
            interest_amount = monthly_payment * sku_item - loan_amount
        else:
            monthly_payment = loan_amount/sku_item

        return {
            "monthly_payment": round(monthly_payment,2),
            "interest_amount": round(interest_amount,2),
        }
    elif PAYMENT_METHOD['100LOAN'] == interest_method:
        monthly_payment = ( loan_amount * monthly_interest_rate * (1+monthly_interest_rate) ** sku_item - final_payment_amount * monthly_interest_rate) / ((1+monthly_interest_rate) ** sku_item - monthly_interest_rate - 1)
        interest_amount = (monthly_payment * (sku_item-1) + final_payment_amount) - loan_amount
        return {
            "monthly_payment": round(monthly_payment,2),
            "interest_amount": round(interest_amount,2),
        }
    else:
        return {
            "monthly_payment": 0,
            "interest_amount": 0,
        }


@redis_func()
def get_lowest_downpay_monthly(city_id=None, series_id=None):
    '''
    获取当前城市指定车系最低的首付和月供
    @param city_id 城市编码
    @param series_id 车系编码
    @return 返回首付和月供两个参数，以及相应的最低首付和最低月供的金融方案ID
    '''
    if not city_id or not series_id:
        logger.error("no city or series")

    resultdict = {}
    params = {}
    params['city_id'] = city_id
    params['series_id'] = series_id

    sql = """
    SELECT
        p.ID,
        MIN(fpp.FIRST_PAY_PERCENT * op.PUBLIC_OFFER_PRICE/100) downpay
    FROM
        t_base_financial_first_pay_percent_rel fpp,
        t_base_financial_product p,
        t_base_financial_dlr_rel fd,
        t_base_financial_series_rel fs,
        t_base_dealer d,
        t_base_offer_price op
    WHERE
        fpp.FINACIAL_PRODUCT_ID = p.ID
        AND p.ID = fd.FINANCIAL_PRODUCT_ID
        AND p.ID = fs.FINANCIAL_PRODUCT_ID
        AND fd.DLR_CODE = d.DLR_CODE
        AND fs.CAR_SERIES_ID = op.CAR_SERIES_ID
        AND d.ID = op.DEALER_ID
        AND d.CITY_ID = %(city_id)s
        AND fs.CAR_SERIES_ID = %(series_id)s
    """
    tmp = db.fetchone(sql, params)
    resultdict['downpay_id'] = tmp['ID']
    resultdict['downpay'] = 0
    if tmp['downpay']:
        resultdict['downpay'] = round(tmp['downpay'], 2)

    sql = """
    SELECT
        p.ID,
        MIN((op.PUBLIC_OFFER_PRICE - fpp.FIRST_PAY_PERCENT * op.PUBLIC_OFFER_PRICE/100) / sku.SKU_ITEM) monthly
    FROM
        t_base_financial_first_pay_percent_rel fpp,
        t_base_financial_pro_sku sku,
        t_base_financial_product p,
        t_base_financial_dlr_rel fd,
        t_base_financial_series_rel fs,
        t_base_dealer d,
        t_base_offer_price op
    WHERE
        fpp.FINACIAL_PRODUCT_ID = p.ID
        AND sku.FINACIAL_PRODUCT_ID = p.id
        AND p.ID = fd.FINANCIAL_PRODUCT_ID
        AND p.ID = fs.FINANCIAL_PRODUCT_ID
        AND fd.DLR_CODE = d.DLR_CODE
        AND fs.CAR_SERIES_ID = op.CAR_SERIES_ID
        AND d.ID = op.DEALER_ID
        AND d.CITY_ID = %(city_id)s
        AND fs.CAR_SERIES_ID = %(series_id)s
    """
    tmp = db.fetchone(sql, params)
    resultdict['monthly_id'] = tmp['ID']
    resultdict['monthly'] = 0
    if tmp['monthly']: resultdict['monthly'] = round(tmp['monthly'], 2)

    return resultdict

@redis_func()
def get_lowest_summary(price=0, city_id=None, series_id=None):
    '''
    获取最低的成本数值
    @param price 经销商报价，输入0即取官方指导价
    @param city_id 城市编码
    @param series_id 车系编码
    @return 返回首付比率、金额，贷款期限、金额，总成本、月供
    '''
    tmp = get_lowest_downpay_monthly(city_id=city_id, series_id=series_id)
    sql = """
    SELECT
        b.FINAL_PAYMENT_SCALE,
        MIN(a.SKU_ITEM) SKU_ITEM,
        a.SKU_RATE
    FROM
        t_base_financial_pro_sku a
    LEFT JOIN t_base_financial_product b ON a.FINACIAL_PRODUCT_ID=b.ID
    WHERE
        a.FINACIAL_PRODUCT_ID=%(product_id)s
    """
    params = {}
    params['product_id'] = tmp['downpay_id']

    tmp = db.fetchone(sql, params)
    resultdict = {}
    resultdict['downpay_scale'] = tmp['FINAL_PAYMENT_SCALE']
    if not tmp['FINAL_PAYMENT_SCALE'] or float(tmp['FINAL_PAYMENT_SCALE']) <= 0: tmp['FINAL_PAYMENT_SCALE'] = 0
    resultdict['downpay_money'] = round(float(tmp['FINAL_PAYMENT_SCALE']) * float(price) / 100, 2)
    resultdict['period'] = tmp['SKU_ITEM']
    resultdict['loan_money'] = round(float(price) - float(resultdict['downpay_money']), 2)
    resultdict['total_cost'] = round(float(resultdict['downpay_money']) * float(tmp['SKU_RATE']) / 100 + float(price), 2)
    resultdict['monthly'] = round(resultdict['total_cost'] / resultdict['period'], 2)
    return resultdict

@redis_func()
def get_downpay_monthly_count(city_id=None):
    '''
    用于获取首页特定城市全车系和相应的首付月供和金融方案数量
    @param city_id 城市编码
    @return 返回首付月供和金融方案名称
    '''
    sql = """
        SELECT
            distinct
            series.id  series_id,
            series.car_series_cn series_name,
            series.pc_thumbnail series_img,
            fpp.first_pay_percent,
            series.start_guideprice public_offer_price,
            sku.sku_rate,
            sku.sku_item,
            p.is_final_payment,
            p.final_payment_scale,
            p.repayment_type,
            ( select count(1) from t_base_financial_series_rel where is_enable=1 and car_series_id=series.id) count
        FROM
            t_base_financial_first_pay_percent_rel fpp,
            t_base_financial_product p,
            t_base_financial_dlr_rel fd,
            t_base_financial_pro_sku sku,
            t_base_financial_series_rel fs,
            t_base_car_series series
        WHERE
            fpp.FINACIAL_PRODUCT_ID = p.ID
            AND p.ID = fd.FINANCIAL_PRODUCT_ID
            AND p.ID = fs.FINANCIAL_PRODUCT_ID
            AND sku.FINACIAL_PRODUCT_ID = p.id
            AND fs.CAR_SERIES_ID = series.id
            and series.is_enable=1
            and series.is_show=1
            and p.id in (249, 252)
            and p.is_enable=1
            and p.EFFECT_START_DATE <= now()
            and p.EFFECT_END_DATE >= now()
            and fpp.FIRST_PAY_PERCENT=50
            and sku.sku_item = 24
            order by series.order_no desc
            limit 8;
    """

    items = db.fetch(sql)

    for item in items:
        '''
            first_pay_percent   首付比例
            sku_item            期数
            sku_rate            年利率
            public_offer_price  价格
            is_final_payment    是否尾款产品
            final_payment_scale 尾款比例
            repayment_type      还款方式
        '''
        _item = item.copy()
        _item = calc_financial(**_item)
        item['downpay'] = round(to_float(_item['public_offer_price']) * 0.3, 2)
        item['monthly'] = _item['monthly_pay_amount']
    return items

@redis_func()
def get_downpays(series_id=None):
    '''
    由车系获取所有可选的首付比例，这个可暂不实现，前端固定为几个比率即可
    @param series_id 车系ID
    @return 所有可选的首付比例
    '''
    sql = """
    SELECT DISTINCT
        fpp.FIRST_PAY_PERCENT
    FROM
        t_base_financial_first_pay_percent_rel fpp,
        t_base_financial_product p,
        t_base_financial_series_rel fs
    WHERE
        fpp.FINACIAL_PRODUCT_ID = p.ID
    AND p.ID = fs.FINANCIAL_PRODUCT_ID
    AND fs.CAR_SERIES_ID = %(series_id)s
    GROUP BY
        fpp.FIRST_PAY_PERCENT
    ORDER BY
        fpp.FIRST_PAY_PERCENT ASC
    """
    params = {}
    params['series_id'] = series_id
    return db.fetch_col_array(sql, params, 'FIRST_PAY_PERCENT')


@redis_func()
def get_periods(series_id=None):
    '''
    由车系获取所有可选的期限，这个可暂不实现，前端固定为几个期限即可
    @param series_id 车系ID
    @return 所有可选的期限
    '''
    sql = """
    SELECT DISTINCT
        sku.SKU_ITEM
    FROM
        t_base_financial_pro_sku sku,
        t_base_financial_product p,
        t_base_financial_series_rel fs
    WHERE
        sku.FINACIAL_PRODUCT_ID = p.ID
    AND p.ID = fs.FINANCIAL_PRODUCT_ID
    AND fs.CAR_SERIES_ID = %(series_id)s
    GROUP BY
        sku.SKU_ITEM
    ORDER BY
        sku.SKU_ITEM ASC
    """
    params = {}
    params['series_id'] = series_id
    return db.fetch_col_array(sql, params, 'SKU_ITEM')


@redis_func()
def get_purchasetax_totalfee(price=0, halftax=False):
    '''
    由车系计算购置税额和购车成本
    @param price 经销商报价
    @param halftax 是否购置税减半车型
    @return 购置税/购车成本
    '''
    if not price:
        logger.error('no price')

    resultdict = {}
    price = float(price)

    purchasetax = price / (1 + 0.17) * 0.1 # 购置税＝购车款/(1+17%)×购置税率(10%)
    if halftax: purchasetax /= 2 # 判断购置税减半

    resultdict['purchasetax'] = round(purchasetax, 2) # 购置税
    resultdict['totalfee'] = round(resultdict['purchasetax'] + price, 2) # 总费用
    return resultdict


@redis_func()
def get_purchasetax(price=0, car_type_id=0):
    '''
        flag 0：正常，1：购置税减半
    '''
    sql="""
        select
        count(1) as cnt
        from T_BASE_CAR_TYPE
        where
        characteristic_activity like %(saving_half)s and
        id = %(car_type_id)s and
        is_enable=1;
    """
    params = {}
    params['car_type_id'] = car_type_id
    params['saving_half'] = '%,24,%' #购置税减半为24
    tmp = db.fetchone(sql, params)

    rtn = {
        'purchasetax': round(to_float(price) / (1 + 0.17) * 0.1, 2),
        'flag': 0
    }
    if tmp and tmp['cnt'] > 0:
        rtn['purchasetax'] = round(rtn['purchasetax']/2, 2)
        rtn['flag'] = 1

    return rtn


# DealsLoan
def get_credit_dnaf_save(**kwargs):
    '''
    日产金融征信资料保存
    '''
    api_address = 'http://172.26.152.176/cbbweb/DealsLoan.do?action=save'
    if not settings.DEBUG:
        api_address = 'http://fun.chebaba.com/api/DealsLoan.do?action=save'
    return requests.post(api_address, data=kwargs).text

def get_credit_dnaf_query(**kwargs):
    '''
    日产金融征信申请
    '''
    api_address = 'http://172.26.152.176/cbbweb/DealsLoan.do?action=query'
    if not settings.DEBUG:
        api_address = 'http://fun.chebaba.com/api/DealsLoan.do?action=query'
    return requests.post(api_address, data=kwargs).text

def get_credit_cmbc_save(**kwargs):
    '''
    招行征信申请：保存资料+获取验证码
    '''
    api_address = 'http://172.26.152.176/cbbweb/DealsLoan.do?action=cmbSave'
    if not settings.DEBUG:
        api_address = 'http://fun.chebaba.com/api/DealsLoan.do?action=cmbSave'
    return requests.post(api_address, data=kwargs).text

def get_credit_cmbc_query(**kwargs):
    '''
    招行征信申请：获取征信额度
    '''
    api_address = 'http://172.26.152.176/cbbweb/DealsLoan.do?action=cmbQuery'
    if not settings.DEBUG:
        api_address = 'http://fun.chebaba.com/api/DealsLoan.do?action=cmbQuery'
    return requests.post(api_address, data=kwargs).text

@redis_func()
def get_financials(price=0, downpay=0, period=0, series_id=0, orderby=0):
    '''
    由车系、首付和月供获取所有金融方案
    @param price 输入报价
    @param downpay 首付比例
    @param period 期数
    @param orderby 排序规则，0:不排序，1:月供价格，2:热门程度 —— 暂未实现
    @return 金融方案列表: LOGO/机构名称/方案名称/方案ID/特点/最低月供/总利息成本/是否尾款产品/尾款比例/申请条件/通过率
    '''
    sql = """
    SELECT
        a.ID,
        b.CORP_LOGO,
        b.CORP_NAME,
        '' CONDITIONS,
        '' MATERIALS,
        a.FINANCIAL_PRODUCT_NAME,
        a.CONTAINS_INTEREST,
        a.PASS_PERCENT,
        c.SKU_RATE TOTAL_COST,
        a.IS_FINAL_PAYMENT,
        a.FINAL_PAYMENT_SCALE,
        c.SKU_ITEM
    FROM
        t_base_financial_product a
    LEFT JOIN t_base_financial_corp b on a.FINANCIAL_CORP_ID=b.ID
    LEFT JOIN t_base_financial_pro_sku c ON a.ID=c.FINACIAL_PRODUCT_ID
    left join t_base_financial_series_rel d on a.id=d.FINANCIAL_PRODUCT_ID
    WHERE
    a.FINAL_PAYMENT_SCALE >= %(downpay)s AND c.SKU_ITEM >= %(period)s
    and d.car_series_id=%(series_id)s
    """

    params = {}
    params['downpay'] = downpay
    params['period'] = period
    params['series_id'] = series_id

    items = db.fetch(sql, params)
    for item in items:
        sql = "SELECT CONDITION_NAME FROM t_base_financial_condition_rel WHERE FINACIAL_PRODUCT_ID = " + str(item['ID']) + " GROUP BY CONDITION_NAME"
        item['CONDITIONS'] = db.fetch_col_array(sql,{},'CONDITION_NAME')
        sql = "SELECT MATERIAL_NAME FROM t_base_financial_material_rel WHERE FINACIAL_PRODUCT_ID = " + str(item['ID']) + " GROUP BY MATERIAL_NAME"
        item['MATERIALS'] = db.fetch_col_array(sql,{},'MATERIAL_NAME')
        item['TOTAL_COST'] = round(float(item['FINAL_PAYMENT_SCALE']) * float(price) / 100, 2)

        plus = 0
        if item['CONTAINS_INTEREST'] and int(item['CONTAINS_INTEREST']) == 1: plus = item['TOTAL_COST']
        item['MONTHLY'] = int((plus + float(price)) / item['SKU_ITEM'])

    return items


@redis_func()
def get_cartype_tax_insurance(car_type_id=0):
    # 获取排量
    displacement = 1600
    sql = """
        SELECT property_value
        FROM e4sdb_data.t_base_car_type_property
        where property_id in
            (SELECT id FROM e4sdb_data.t_base_car_type_property_template
            where property_key in ('pailiang_cc'))
            and car_type_id = %(car_type_id)s;
    """

    params = {}
    params['car_type_id'] = car_type_id
    item = db.fetchone(sql, params)
    if item and item['property_value']:
        displacement = to_int(item['property_value'])

    rtn = {
        'travel_tax': 0,
        'travel_insurance': 950,
        'busi_insurance': 2065
    }

    if displacement in range(1, 1001):
        rtn['travel_tax'] = 180
    elif displacement in range(1001,1601):
        rtn['travel_tax'] = 360
    elif displacement in range(1601,2001):
        rtn['travel_tax'] = 420
    elif displacement in range(2001,2501):
        rtn['travel_tax'] = 720
    elif displacement in range(3001,4001):
        rtn['travel_tax'] = 3000
    elif displacement > 4000:
        rtn['travel_tax'] = 4500

    return rtn
