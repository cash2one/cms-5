# -*- coding: utf-8 -*-

import random

from cbbweb.core.utils import str2array
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
def get_car_series_by_id(car_series_id=None):
    """
        根据车系ID获取车系基本数据

        参数
        ----
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            车系基本数据
    """
    car_series_id = common_utils.to_int(car_series_id)
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_series_id
    )
    return car_series


@redis_func()
def get_car_series_data(city_id=None, car_series_id=None):
    """
        车系页面，PC和WAP通用。
        根据城市ID，车系ID获取车系对应的基本数据，活动，报价

        参数
        ----
        city_id : int
            城市ID
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            报价是当前城市的最低经销商报价，
            如果当前城市ID和车系ID没有经销商报价，
            price用车系的厂家最低价start_guideprice代替
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_series_id
    )
    if not car_series:
        return None
    car_brand = car_brand_utils.get_carbrand_by_id(car_series['car_brand_id'])
    if not car_brand:
        return None
    activity_list = activity_utils.get_activity_list_by_city_series(
        city_id=city_id,
        car_series_id=car_series_id
    )
    for activity in activity_list:
        activity['dealer'] = dealer_utils.get_dealer_by_id(
            dealer_id=activity['dealer_id']
        )
    result_dict = {
        'brand': car_brand,
        'series': car_series,
        'activity_list': activity_list,
    }

    offer_price = offer_price_utils.get_offerprice(
        city_id=city_id,
        car_series_id=car_series_id,
    )
    result_dict['series']['offer_price'] = offer_price

    return result_dict


@redis_func()
def get_car_series_property(car_series_id=None, prop_keys=None):
    """
        车系页面，PC和WAP通用
        获取车系下所有车型的多个属性

        参数
        ----
        car_series_id : int
            车系ID
        prop_keys : list of str
            属性对应的字符串数组，例如['pailiang', 'chang']

        返回值
        ------
        result_dict : dict
            每个属性的KEY对应的是一个数组，
            对应的是所有车型的不同的值
    """
    if not prop_keys:
        return None
    car_series_id = common_utils.to_int(car_series_id)

    prop_keys = str2array(prop_keys)

    cursor = connection().cursor()
    car_series_sql = """
        SELECT 
            a.order_no, a.property_key, a.name, b.property_value 
        FROM 
            t_base_car_type_property_template AS a, 
            t_base_car_type_property AS b, 
            t_base_car_type AS c 
        WHERE 
            a.id=b.property_id 
            AND b.car_type_id=c.id 
            AND c.car_series_id=%s 
            AND a.property_key in %s
            AND a.is_enable=1
            AND b.is_enable=1
            AND c.is_enable=1
            AND c.is_show=1
    """
    cursor.execute(car_series_sql, [car_series_id, prop_keys])
    rows = dictfetchall(cursor)
    prop_dict = {}
    for row in rows:
        key = row['property_key']
        if key not in prop_dict:
            prop_dict[key] = []
            prop_dict[key].append(row)
        else:
            is_contained = False
            for prop in prop_dict[key]:
                if prop['property_value'] == row['property_value']:
                    is_contained = True
                    break
            if not is_contained:
                prop_dict[key].append(row)
    return prop_dict

@redis_func(timeout=1)
def get_hot_car_series(city_id=None, count=5):
    """
        PC端车系和车型页面,
        随机获取count个车系基本数据

        参数
        ----
        city_id : int, 没用
            城市ID，只是为了接口兼容留着，不用传
        count : int
            要随机获取的数量

        返回值
        ------
        result_list : list
            返回车系数组
    """
    city_id = common_utils.to_int(city_id)
    series_list = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                            is_enable=1, is_show=1,
                            pc_thumbnail__isnull=False)

    series_count = series_list.count()
    if series_count <= 0:
        return None
    count = common_utils.max_int(count)

    result_list = []
    offset = random.randint(0, series_count)
    rand_max = 2
    if series_count > count:
        rand_max = int((series_count - count) / count)
    if rand_max < 2:
        rand_max = 2
    for rand_count in range(count):
        offset = (offset + random.randint(1, rand_max)) % series_count
        series = series_list[offset]
        series_dict = car_series_utils.get_carseries_by_id(
            car_series_id=series.id
        )
        result_list.append(series_dict)
    return result_list


@redis_func()
def get_on_sale_car_types(city_id=None, car_series_id=None,
                          per_page=10, page=1,
                          orderby='price', descending=False):
    """
        车系页面，PC和WAP通用，
        根据城市ID和车系ID获取在售车型，按报价或者优惠排序
        返回值里的financial目前是在PC端用到

        参数
        ----
        city_id : int
            城市ID
        car_series_id : int
            车系ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码
        orderby : {'price', 'discount'}
            price按报价排序，discount按优惠排序
        descending : {0, 1}
            0按升序，1按降序

        返回值
        ------
        result_dict : dict
            返回车系基本数据和车型数组
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    orderby_price = True
    if orderby == 'discount':
        orderby_price = False
    else:
        orderby_price = True
    if descending:
        if isinstance(descending, str) and (descending.upper() != 'TRUE'):
            descending = False
    
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_series_id
    )
    if not car_series:
        return None

    car_type_id_list = car_type_utils.get_cartype_id_list_by_series(
        car_series_id=car_series_id
    )
    if not car_type_id_list:
        return None
    
    car_type_list = []
    for car_type_id in car_type_id_list:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=car_type_id
        )
        if not tmp_car_type:
            continue
        tmp_offer_price = offer_price_utils.get_offerprice(
            city_id=city_id,
            car_type_id=car_type_id
        )
        tmp_car_type['offer_price'] = tmp_offer_price
        if 'dealer_id' in tmp_offer_price:
            tmp_dealer = dealer_utils.get_dealer_by_id(tmp_offer_price['dealer_id'])
            tmp_car_type['dealer'] = tmp_dealer
        else:
            tmp_car_type['dealer'] = None

        financial = get_lowest_monthly_payment(
            city_id=city_id,
            car_series_id=car_series_id,
            car_type_id=car_type_id,
            price=tmp_car_type['offer_price']['price']
        )
        tmp_car_type['financial'] = financial

        car_type_list.append(tmp_car_type)
    if car_type_list:
        car_type_list = offer_price_utils.sorted_offer_price_list(
            offer_price_list=car_type_list,
            orderby_price=orderby_price,
            descending=descending
        )
        car_type_list = car_type_list[offset: (offset+count)]
    result_dict = {
        'series': car_series,
        'car_type_list': car_type_list
    }
    return result_dict


@redis_func()
def get_car_series_dealer(city_id=None, county_id=None, car_series_id=None,
                          per_page=10, page=1,
                          orderby='price', descending=False):
    """
        WAP端车系页面
        返回对应城市、县区和车系的经销商

        参数
        ----
        city_id : int
            城市ID
        county_id : int, 可选
            县区ID
        car_series_id : int
            车系ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码
        orderby : {'price', 'discount'}
            price按报价排序，discount按优惠排序
        descending : {0, 1}
            0按升序，1按降序

        返回值
        ------
        result_list : list
            返回经销商数组，包括对应车系的促销活动
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    car_series_id = common_utils.to_int(car_series_id)
    orderby_price = True
    if orderby == 'discount':
        orderby_price = False
    else:
        orderby_price = True
    if descending:
        if isinstance(descending, str) and (descending.upper() != 'TRUE'):
            descending = False

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        county_id=county_id,
        car_series_id=car_series_id
    )
    if not dealer_id_list:
        return None
    result_list = []
    for dealer_id in dealer_id_list:
        tmp_dealer = dealer_utils.get_dealer_by_id(dealer_id=dealer_id)
        if not tmp_dealer:
            continue
        tmp_dealer['offer_price'] = offer_price_utils.get_offerprice(
            city_id=city_id,
            dealer_id=tmp_dealer['id'],
            car_series_id=car_series_id
        )
        activity_list = activity_utils.get_activity_list_by_dealer_series(
            dealer_id=tmp_dealer['id'],
            car_series_id=car_series_id
        )
        tmp_dealer['activity_list'] = activity_list
        result_list.append(tmp_dealer)
    if result_list:
        result_list = offer_price_utils.sorted_offer_price_list(
            offer_price_list=result_list,
            orderby_price=orderby_price,
            descending=descending
        )
        result_list = result_list[offset: (offset+count)]
    return result_list

@redis_func()
def get_group_series_car_types(car_series_id=None, property_key=None):
    """
        PC端车系页面、车型页面
        WAP端车型页面
        用在更换车型的列表
        根据车系ID获取所有车型，然后根据property_key属性进行分组排序

        参数
        ----
        car_series_id : int
            车系ID
        property_key : str
            车系下的车型按什么属性分组，例如'pailiang'按排量分组

        返回值
        ------
        result_list : list
            返回车系下所有车型，然后根据property_key属性进行分组
    """
    car_series_id = common_utils.to_int(car_series_id)
    car_types = list_objs(model=ModelName.T_BASE_CAR_TYPE,
                          is_enable=1, is_show=1,
                          car_series_id=car_series_id)
    if not car_types:
        return None
    car_ids = list(car_types.values_list('id', flat=True))
    car_type_prop = get_object(
        model=ModelName.T_BASE_CAR_TYPE_PROPERTY_TEMPLATE,
        is_enable=1,
        property_key=property_key
    )
    if not car_type_prop:
        return None
    car_props = list_objs(model=ModelName.T_BASE_CAR_TYPE_PROPERTY,
                          orderby=['property_value'],
                          is_enable=1,
                          property_id=car_type_prop.id,
                          car_type_id__in=car_ids)
    if not car_props:
        return None
    car_type_dict = {}
    for car_type in car_types:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=car_type.id
        )
        car_type_dict[car_type.id] = tmp_car_type
    car_dict = {}
    for car_prop in car_props:
        key = car_prop.property_value
        if key in car_dict:
            car_dict[key].append(car_type_dict[car_prop.car_type_id])
        else:
            car_dict[key] = []
            car_dict[key].append(car_type_dict[car_prop.car_type_id])
    dict_keys = car_dict.keys()
    sorted_dict_keys = sorted(dict_keys)
    data_list = []
    for key in sorted_dict_keys:
        data_dict = {
            'value': key,
            'car_type_list': car_dict[key]
        }
        data_list.append(data_dict)
    return data_list

@redis_func()
def get_car_series_search():
    """
        页面右上角车系搜索列表，
        只显示t_cms_catalogs里的as_search_result为1的车系，最多返回10个

        参数
        ----
        None : None
            无

        返回值
        ------
        result_list : list
            返回车系数组，根据t_cms_catalogs里的vieworder排序
    """
    car_series_catalogs = list_objs(model=ModelName.T_CMS_CATALOGS,
                                    orderby=['vieworder'],
                                    count=10,
                                    is_enable=1,
                                    as_search_result=1,
                                    model_table='t_base_car_series')
    if not car_series_catalogs:
        return []
    result_list = []
    for csc in car_series_catalogs:
        car_series = car_series_utils.get_carseries_by_id(
            car_series_id=csc.model_instanceid
        )
        if car_series:
            result_list.append(car_series)
    return result_list

