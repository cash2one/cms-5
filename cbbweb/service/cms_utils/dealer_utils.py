# -*- coding: utf-8 -*-


from jinja2 import Template

from django.conf import settings

from cbbweb.core.utils import str2array
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.db import connection
from cbbweb.core.utils.db import dictfetchall

from cbbweb.service import get_object
from cbbweb.service.catalogs_service import URL
from cbbweb.service.catalogs_service import get_cms_sub_url
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import activity_utils
from cbbweb.service.cms_utils import car_brand_utils
from cbbweb.service.cms_utils import place_utils

DEALER_DEFAULT_IMG_URL = (settings.STATIC_URL 
                          + 'site/images/lib/dealer_default.jpg')

@redis_func()
def service_auth(tmp_service_auth):
    """
        经销商_服务认证
    """
    if not tmp_service_auth:
        return []
    dict_group = get_object(model=ModelName.T_BASE_DATA_DICT_GROUP,
                            is_enable=1, is_show=1,
                            dictgroup_name='serviceCertify')
    if not dict_group:
        return []
    dict_group_id = dict_group.id
    service_auth_list = tmp_service_auth.split(',')
    prop_list = []
    for service_auth_key in service_auth_list:
        if service_auth_key:
            prop = get_object(model=ModelName.T_BASE_DATA_DICT,
                              is_enable=1, is_show=1,
                              dictgroup_id=dict_group_id,
                              dict_key=service_auth_key)
            prop_list.append(prop.dict_value)
        else:
            prop_list.append(None)
    return prop_list

@redis_func()
def car_series_ids(tmp_car_series_ids):
    """
        在售车系数组
    """
    if not tmp_car_series_ids:
        return []
    result_list = []
    car_series_id_list = tmp_car_series_ids.split(',')
    for tmp_id in car_series_id_list:
        tmp_id = common_utils.to_int(tmp_id)
        if tmp_id:
            result_list.append(tmp_id)
    return result_list



@redis_func()
def cbb_car_brand_code(tmp_cbb_car_brand_code):
    '''
        车巴巴经营品牌
    '''
    if not tmp_cbb_car_brand_code:
        return []
    prop_list = []
    cbb_car_brand_code_list = tmp_cbb_car_brand_code.split(',')
    for cbb_car_brand_code_key in cbb_car_brand_code_list:
        if cbb_car_brand_code_key:
            car_brand_id = int(cbb_car_brand_code_key)
            tmp_car_brand = car_brand_utils.get_carbrand_by_id(
                car_brand_id=car_brand_id
            )
            if tmp_car_brand:
                prop_list.append(tmp_car_brand['name'])
    return prop_list

@redis_func()
def is_sale_province(sale_city_ids):
    '''
        是否售本省
    '''
    if not sale_city_ids:
        return 0
    if sale_city_ids.startswith('2,'):
        return 1
    return 0
@redis_func()
def province_name(province_id):
    """
        省名字
    """
    if not province_id:
        return ""
    province = place_utils.get_province_by_id(
        province_id=province_id
    )
    if not province:
        return ""
    return province['province_name']

@redis_func()
def city_name(city_id):
    """
        城市名字
    """
    if not city_id:
        return ""
    city = place_utils.get_city_by_id(
        city_id=city_id
    )
    if not city:
        return ""
    return city['city_name']


@redis_func()
def county_name(county_id):
    '''
        县区名字
    '''
    if not county_id:
        return ""
    county = place_utils.get_county_by_id(
        county_id=county_id
    )
    if not county:
        return ""
    return county['county_name']

@redis_func()
def get_dealer_by_id(dealer_id=None):
    """
        根据经销商ID返回经销商实例
    """
    dealer_id = common_utils.to_int(dealer_id)
    tmp_dealer = get_object(model=ModelName.T_BASE_DEALER,
                            is_enable=1, is_frozen=0,
                            id=dealer_id)
    if not tmp_dealer:
        return None
    activity_list = activity_utils.get_activity_list_by_dealer(
        dealer_id=tmp_dealer.id
    )
    pre_sales_score = common_utils.to_int(tmp_dealer.pre_sales_score)
    after_sales_score = common_utils.to_int(tmp_dealer.after_sales_score)
    sales_score = (pre_sales_score + after_sales_score) / 2
    province_id = common_utils.to_int(tmp_dealer.province_id)
    city_id = common_utils.to_int(tmp_dealer.city_id)
    county_id = common_utils.to_int(tmp_dealer.county_id)
    dealer_dict = {
        'id': tmp_dealer.id,
        'dlr_code': tmp_dealer.dlr_code,
        'url': get_cms_sub_url(URL.DEALER, tmp_dealer.id),
        'dlr_short_name': tmp_dealer.dlr_short_name,
        'dlr_full_name': tmp_dealer.dlr_full_name,
        'dlr_prop': tmp_dealer.dlr_prop,
        'parent_dlr_id': tmp_dealer.parent_dlr_id,
        'dlr_status': tmp_dealer.dlr_status,
        'dlr_level': tmp_dealer.dlr_level,
        'car_series_ids': car_series_ids(tmp_dealer.car_series_ids),
        'sale_city_ids': tmp_dealer.sale_city_ids,
        'is_sale_province': is_sale_province(tmp_dealer.sale_city_ids),
        'group_id': tmp_dealer.group_id,
        'email': tmp_dealer.email,
        'sale_tel': tmp_dealer.sale_tel,
        'service_tel': tmp_dealer.service_tel,
        'service_tel_sub': tmp_dealer.service_tel_sub,
        'cbb_car_brand_code': cbb_car_brand_code(tmp_dealer.cbb_car_brand_code),
        'is_vip': tmp_dealer.is_vip,
        'service_auth': service_auth(tmp_dealer.service_auth),
        'pre_sales_score': pre_sales_score,
        'after_sales_score': after_sales_score,
        'sales_score': sales_score,
        'pre_sales_score_prop': tmp_dealer.pre_sales_score_prop,
        'after_sales_score_prop': tmp_dealer.after_sales_score_prop,
        'dlr_image_url': tmp_dealer.dlr_image_url,
        'province_id': province_id,
        'province_name': province_name(province_id),
        'city_id': city_id,
        'city_name': city_name(city_id),
        'county_id': county_id,
        'county_name': county_name(county_id),
        'cont_address': tmp_dealer.cont_address,
        'zip_code': tmp_dealer.zip_code,
        'longitude': common_utils.to_float(tmp_dealer.longitude),
        'latitude': common_utils.to_float(tmp_dealer.latitude),
        'order_no': tmp_dealer.order_no,

        'dealer_activity_list': activity_list,
    }

    if not dealer_dict['dlr_image_url']:
        dealer_dict['dlr_image_url'] = DEALER_DEFAULT_IMG_URL

    return dealer_dict

@redis_func()
def get_dealer_list_by_id_list(dealer_id_list=None):
    dealer_id_list = str2array(dealer_id_list)
    if not dealer_id_list:
        return None
    dealer_list = []
    for dealer_id in dealer_id_list:
        tmp_dealer = get_dealer_by_id(dealer_id=dealer_id)
        if tmp_dealer:
            dealer_list.append(tmp_dealer)
    return dealer_list

@redis_func()
def get_dealer_id_list_by_nation(car_brand_id=None, car_series_id=None):
    """
        查找 sale_city_ids 售全国 '1'
    """
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            AND sale_city_ids='1'
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        return None
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_sale_province(province_id=None,
                                        car_brand_id=None,
                                        car_series_id=None):
    """
        查找 sale_city_ids 售全省 '2,123'
    """
    province_id = common_utils.to_int(province_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if province_id %} 
                AND sale_city_ids='2,{{province_id}}'
            {% endif %}
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'province_id': province_id,
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        # 查找 sale_city_ids 售全国 '1'
        return get_dealer_id_list_by_nation(car_brand_id=car_brand_id,
                                            car_series_id=car_series_id)
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_province(province_id=None,
                                   car_brand_id=None,
                                   car_series_id=None):
    """
        根据省ID
    """
    province_id = common_utils.to_int(province_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if province_id %} 
                AND province_id={{province_id}}
            {% endif %}
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'province_id': province_id,
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        # 查找 sale_city_ids 售全国 '1'
        return get_dealer_id_list_by_nation(car_brand_id=car_brand_id,
                                            car_series_id=car_series_id)
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_multy_city(city_id=None,
                                     car_brand_id=None,
                                     car_series_id=None):
    """
        查找 sale_city_ids 为多个城市 '4,123,456,'
    """
    city_id = common_utils.to_int(city_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if city_id %} 
                AND sale_city_ids like '4%,{{city_id}},%'
            {% endif %}
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'city_id': city_id,
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        # 查找 sale_city_ids 售全省 '2,123'
        city_info = place_utils.get_city_by_id(city_id=city_id)
        if not city_info:
            return None
        province_id = city_info['province_id']
        return get_dealer_id_list_by_sale_province(province_id=province_id,
                                                   car_brand_id=car_brand_id,
                                                   car_series_id=car_series_id)
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_city(city_id=None,
                               car_brand_id=None,
                               car_series_id=None):
    """
        查找city_id
    """
    city_id = common_utils.to_int(city_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if city_id %} 
                AND city_id={{city_id}} 
            {% endif %}
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'city_id': city_id,
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        # 查找 sale_city_ids 为多个城市 '4,123,456'
        return get_dealer_id_list_by_multy_city(city_id=city_id,
                                                car_brand_id=car_brand_id,
                                                car_series_id=car_series_id)
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_county(county_id=None,
                                 car_brand_id=None,
                                 car_series_id=None):
    """
        根据县区ID查找
    """
    county_id = common_utils.to_int(county_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if county_id %} 
                AND county_id={{county_id}} 
            {% endif %}
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'county_id': county_id,
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        # 根据城市ID查找
        county_info = place_utils.get_county_by_id(county_id=county_id)
        if not county_info:
            return None
        city_id = county_info['city_id']
        return get_dealer_id_list_by_city(city_id=city_id,
                                          car_brand_id=car_brand_id,
                                          car_series_id=car_series_id)
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list_by_car(car_brand_id=None,
                              car_series_id=None):
    """
        根据县区ID查找
    """
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    dealer_sql_template = '''
        SELECT 
            id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            {% if car_series_id %} 
                AND car_series_ids like '%,{{car_series_id}},%'
            {% elif car_brand_id %} 
                AND cbb_car_brand_code like '%,{{car_brand_id}},%'
            {% endif %}
    '''
    param = {
        'car_brand_id': car_brand_id,
        'car_series_id': car_series_id,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql)
    dealer_list = dictfetchall(cursor)
    if not dealer_list:
        return None
    dealer_id_list = []
    for tmp_dealer in dealer_list:
        dealer_id_list.append(tmp_dealer['id'])
    return dealer_id_list

@redis_func()
def get_dealer_id_list(province_id=None, city_id=None, county_id=None,
                       car_brand_id=None, car_series_id=None):
    """
        根据省ID或者城市ID或者县区ID或者品牌ID或者车系ID返回经销商ID数组

        参数
        ----
        province_id : int, 可选
            省ID
        city_id : int, 可选
            城市ID
        county_id : int, 可选
            县区ID
        car_brand_id : int, 可选
            品牌ID
        car_series_id : int, 可选
            车系ID

        返回值
        ------
        result_list : list
            经销商ID数组
    """
    province_id = common_utils.to_int(province_id)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    car_brand_id = common_utils.to_int(car_brand_id)
    car_series_id = common_utils.to_int(car_series_id)
    if county_id:
        return get_dealer_id_list_by_county(county_id=county_id,
                                            car_brand_id=car_brand_id,
                                            car_series_id=car_series_id)
    elif city_id:
        return get_dealer_id_list_by_city(city_id=city_id,
                                          car_brand_id=car_brand_id,
                                          car_series_id=car_series_id)
    elif province_id:
        return get_dealer_id_list_by_province(province_id=province_id,
                                              car_brand_id=car_brand_id,
                                              car_series_id=car_series_id)
    else:
        return get_dealer_id_list_by_car(car_brand_id=car_brand_id,
                                         car_series_id=car_series_id)

@redis_func()
def get_dealer_list(province_id=None, city_id=None, county_id=None,
                    car_brand_id=None, car_series_id=None):
    """
        根据省ID或者城市ID或者县区ID或者品牌ID或者车系ID返回经销商基础数据数组

        参数
        ----
        province_id : int, 可选
            省ID
        city_id : int, 可选
            城市ID
        county_id : int, 可选
            县区ID
        car_brand_id : int, 可选
            品牌ID
        car_series_id : int, 可选
            车系ID

        返回值
        ------
        result_list : list
            经销商基础数据数组
    """
    return get_dealer_list_by_id_list(
        get_dealer_id_list(province_id=province_id,
                           city_id=city_id,
                           county_id=county_id,
                           car_brand_id=car_brand_id,
                           car_series_id=car_series_id)
    )

@redis_func()
def get_dealer_count(province_id=None, city_id=None, county_id=None,
                     car_brand_id=None, car_series_id=None):
    """
        根据省ID或者城市ID或者县区ID或者品牌ID或者车系ID返回经销商数量

        参数
        ----
        province_id : int, 可选
            省ID
        city_id : int, 可选
            城市ID
        county_id : int, 可选
            县区ID
        car_brand_id : int, 可选
            品牌ID
        car_series_id : int, 可选
            车系ID

        返回值
        ------
        result_list : list
            经销商数量
    """
    return len(get_dealer_id_list(province_id=province_id,
                                  city_id=city_id,
                                  county_id=county_id,
                                  car_brand_id=car_brand_id,
                                  car_series_id=car_series_id))


