# -*- coding: utf-8 -*-


from jinja2 import Template

from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.db import connection
from cbbweb.core.utils.db import dictfetchall

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.financial_service import get_lowest_monthly_payment
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_brand_utils
from cbbweb.service.cms_utils import car_series_utils
from cbbweb.service.cms_utils import car_type_utils
from cbbweb.service.cms_utils import offer_price_utils
from cbbweb.service.cms_utils import activity_utils
from cbbweb.service.cms_utils import dealer_utils


@redis_func()
def get_car_brand_by_id(car_brand_id=None):
    """
        根据品牌ID获取品牌基本数据

        参数
        ----
        car_brand_id : int
            品牌ID

        返回值
        ------
        result_dict : dict
            品牌基本数据字典
    """
    car_brand_id = common_utils.to_int(car_brand_id)
    car_brand = car_brand_utils.get_carbrand_by_id(car_brand_id=car_brand_id)
    return car_brand

@redis_func()
def get_car_brand_list_by_id(car_brand_id=None):
    """
        根据品牌ID获取品牌基本数据，返回的是数组

        参数
        ----
        car_brand_id : int
            品牌ID，0返回所有品牌基本数据数组

        返回值
        ------
        result_list : list
            品牌基本数据，如果car_brand_id=0返回的是所有品牌
    """
    car_brand_id = common_utils.to_int(car_brand_id)
    result_list = []
    if car_brand_id == 0:
        car_brand_list = list_objs(model=ModelName.T_BASE_CAR_BRAND,
                                   is_enable=1, is_show=1)
        if car_brand_list:
            for tmp_car_brand in car_brand_list:
                car_brand_info = car_brand_utils.get_carbrand_by_id(
                    car_brand_id=tmp_car_brand.id
                )
                if car_brand_info:
                    result_list.append(car_brand_info)
        return result_list
    else:
        car_brand_list = list_objs(model=ModelName.T_BASE_CAR_BRAND,
                                   id=car_brand_id,
                                   is_enable=1, is_show=1)
        if car_brand_list:
            for tmp_car_brand in car_brand_list:
                car_brand_info = car_brand_utils.get_carbrand_by_id(
                    car_brand_id=tmp_car_brand.id
                )
                if car_brand_info:
                    result_list.append(car_brand_info)
        return result_list

@redis_func()
def get_car_offical_car_info():
    """
        查询车系信息，以官网车型级别分类

        参数
        ----
        None : None
            无

        返回值
        ------
        result_dict : dict
            返回车系信息，以官网车型级别分类，1是三厢车，2是两厢车，3是SUV，4是原装进口
    """
    official_car_level_group_info = get_object(
        model=ModelName.T_BASE_DATA_DICT_GROUP,
        is_enable=1, is_show=1,
        dictgroup_name='officialCarLevel'
    )
    if not official_car_level_group_info:
        return None
    official_car_level_list = list_objs(
        model=ModelName.T_BASE_DATA_DICT,
        orderby=['sort_order'],
        is_enable=1, is_show=1,
        dictgroup_id=official_car_level_group_info.id
    )
    if not official_car_level_list:
        return None
    result_dict = {}
    official_info_list = []
    for official_cl in official_car_level_list:
        car_series_list = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                                    orderby=['order_no'],
                                    is_enable=1, is_show=1,
                                    official_car_level=official_cl.dict_key)
        if not car_series_list:
            continue
        tmp_info_dict = {
            'official_level_id': official_cl.dict_key,
            'official_level_name': official_cl.dict_value,
            'official_level_sort_order': official_cl.sort_order,
            'car_series_count': car_series_list.count(),
        }
        official_info_list.append(tmp_info_dict)
    result_dict['official_info_list'] = official_info_list
    result_dict['official_info_count'] = len(official_info_list)
    return result_dict

@redis_func()
def get_car_catalog_data(city_id=None, car_type=None, per_page=10, page=1):
    """
        WEB端惠挑车首页.
        根据官网车型级别ID返回车系信息

        参数
        ----
        city_id : int
            城市ID
        car_type : {0, 1, 2, 3, 4}
            官网车型级别参数，0为全部，1是三厢，2是两厢，3是SUV，4是进口
        per_page : int
            当前页要获取的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            根据t_base_car_series的order_no升序排序.
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    car_type = common_utils.to_int(car_type)
    car_series = None
    if car_type == 0:
        car_series = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                               orderby=['order_no'],
                               offset=offset, count=count,
                               is_enable=1, is_show=1)
    else:
        car_series = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                               orderby=['order_no'],
                               offset=offset, count=count,
                               is_enable=1, is_show=1,
                               official_car_level=car_type)
    if not car_series:
        return None

    result_list = []
    for series in car_series:
        car_brand = car_brand_utils.get_carbrand_by_id(
            car_brand_id=series.car_brand_id
        )
        if not car_brand:
            continue
        series_data = {
            'brand': car_brand,
            'series': car_series_utils.get_carseries_by_id(
                car_series_id=series.id
            ),
        }
        series_data['series']['offer_price'] = {}
        series_data['series']['activity_list'] = []

        offer_price = offer_price_utils.get_offerprice(
            city_id=city_id,
            car_series_id=series.id,
        )
        if 'dealer_id' in offer_price:
            series_data['series']['offer_price'] = offer_price
            activity_list = activity_utils.get_activity_list_by_dealer_series(
                dealer_id=offer_price['dealer_id'],
                car_series_id=series.id
            )
            series_data['series']['activity_list'] = activity_list
        else:
            series_data['series']['offer_price'] = {
                'public_offer_price': common_utils.to_int(series.start_guideprice),
                'price': common_utils.to_int(series.start_guideprice),
                'discount': 0,
                'guide_price': common_utils.to_int(series.start_guideprice),
            }
        financial = {}
        financial = get_lowest_monthly_payment(
            city_id=city_id,
            car_series_id=series.id,
            price=series_data['series']['offer_price']['price']
        )
        series_data['series']['financial'] = financial
        result_list.append(series_data)
    return result_list

@redis_func()
def get_car_catalog_brand_data(city_id=None, car_brand_id=None,
                               per_page=10, page=1):
    """
        PC端惠挑车首页.
        根据品牌ID返回车系信息

        参数
        ----
        city_id : int
            城市ID
        car_brand_id : int
            品牌ID
        per_page : int
            当前页要获取的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            根据t_base_car_series的order_no升序排序.
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series = None
    if car_brand_id == 0:
        car_series = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                               orderby=['order_no'],
                               offset=offset, count=count,
                               is_enable=1, is_show=1)
    else:
        car_series = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                               orderby=['order_no'],
                               offset=offset, count=count,
                               is_enable=1, is_show=1,
                               car_brand_id=car_brand_id)
    if not car_series:
        return None
    result_list = []
    for series in car_series:
        car_brand = car_brand_utils.get_carbrand_by_id(
            car_brand_id=series.car_brand_id
        )
        if not car_brand:
            continue
        series_data = {
            'brand': car_brand,
            'series': car_series_utils.get_carseries_by_id(
                car_series_id=series.id
            ),
        }
        series_data['series']['offer_price'] = {}
        series_data['series']['activity_list'] = []

        offer_price = offer_price_utils.get_offerprice(
            city_id=city_id,
            car_series_id=series.id,
        )
        if 'dealer_id' in offer_price:
            series_data['series']['offer_price'] = offer_price
            activity_list = activity_utils.get_activity_list_by_dealer_series(
                dealer_id=offer_price['dealer_id'],
                car_series_id=series.id
            )
            series_data['series']['activity_list'] = activity_list
        else:
            series_data['series']['offer_price'] = {
                'public_offer_price': common_utils.to_int(series.start_guideprice),
                'price': common_utils.to_int(series.start_guideprice),
                'discount': 0,
                'guide_price': common_utils.to_int(series.start_guideprice),
            }
        financial = {}
        financial = get_lowest_monthly_payment(
            city_id=city_id,
            car_series_id=series.id,
            price=series_data['series']['offer_price']['price']
        )
        series_data['series']['financial'] = financial
        result_list.append(series_data)
    return result_list

@redis_func()
def get_car_article_info(city_id=None, article_id=None):
    """
        PC端惠挑车测评文章页.
        通过文章ID和城市ID返回对应的车系，推荐经销商

        参数
        ----
        city_id : int
            城市ID
        article_id : int
            文章ID

        返回值
        ------
        result_dict : dict
            车系按照数据库的顺序排序。
            经销商排序按照 堡垒店-》评分
    """
    city_id = common_utils.to_int(city_id)
    article_id = common_utils.to_int(article_id)
    article_rela_list = list_objs(model=ModelName.T_CMS_ARTICLE_RELA,
                                  # is_enable=1,
                                  type='CAR_SERIES',
                                  article_id=article_id)
    if not article_rela_list:
        return None
    car_series_list = []
    for article_rela in article_rela_list:
        car_series = car_series_utils.get_carseries_by_id(
            car_series_id=article_rela.object_id
        )
        if car_series:
            car_series_list.append(car_series)

    car_series_id = car_series_list[0]['id']
    result_dict = {
        'car_series_list': car_series_list,
        'dealer': utils_dealer_city_series_types(
            city_id=city_id,
            car_series_id=car_series_id
        )
    }
    return result_dict


@redis_func()
def utils_dealer_city_series_types(city_id=None, car_series_id=None, count=2):
    """
        根据城市ID和车系ID返回当前城市的经销商
        排序按照 堡垒店-》评分
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)
    count = common_utils.max_int(count)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        car_series_id=car_series_id
    )
    if not dealer_id_list:
        return None
    dealer_sql_template = '''
        SELECT
            id, (pre_sales_score+after_sales_score)/2 as sales_score
        FROM
            t_base_dealer
        WHERE
            is_enable=1
            AND is_frozen=0
            AND id in ({{dealer_id_list}})
        ORDER BY
            is_vip desc, sales_score desc
        LIMIT
            %(count)s
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
        'count': count,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    dealer_list = []
    for tmp_dealer in dealers:
        tmp_dealer = dealer_utils.get_dealer_by_id(
            dealer_id=tmp_dealer['id']
        )
        # 获取当前经销商的在售车型和报价
        price_sql_template = '''
            SELECT
                id, car_type_id
            FROM
                t_base_offer_price
            WHERE
                dealer_id=%(dealer_id)s
                AND car_series_id=%(car_series_id)s
                AND is_enable = 1
            ORDER BY
                public_offer_price
            LIMIT
                %(count)s
        '''
        param = {
            'dealer_id': tmp_dealer['id'],
            'car_series_id': car_series_id,
            'count': 4,
        }
        price_sql = Template(price_sql_template).render(param)
        cursor = connection().cursor()
        cursor.execute(price_sql, param)
        price_list = dictfetchall(cursor)

        car_type_list = []
        for price in price_list:
            car_type = car_type_utils.get_cartype_by_id(
                car_type_id=price['car_type_id']
            )
            if not car_type:
                continue
            offer_price = offer_price_utils.get_offerprice_by_id(
                offer_price_id=price['id']
            )
            if not offer_price:
                continue
            car_type['offer_price'] = offer_price
            car_type_list.append(car_type)
        tmp_dealer['car_type_list'] = car_type_list

        dealer_list.append(tmp_dealer)
    return dealer_list

