# -*- coding: utf-8 -*-


from jinja2 import Template

from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.db import connection
from cbbweb.core.utils.db import dictfetchall

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import place_utils
from cbbweb.service.cms_utils import car_brand_utils
from cbbweb.service.cms_utils import car_series_utils
from cbbweb.service.cms_utils import car_type_utils
from cbbweb.service.cms_utils import offer_price_utils
from cbbweb.service.cms_utils import dealer_utils



@redis_func()
def get_group_brand_car_series():
    """
        PC端任性贷首页选择车系
        返回所有车系，按品牌排序

        参数
        ----
        None : None
            无

        返回值
        ------
        result_list : list
            返回所有车系，按品牌排序
    """
    brand_list = list_objs(model=ModelName.T_BASE_CAR_BRAND,
                           is_enable=1, is_show=1)
    brand_ids = brand_list.values_list('id', flat=True)
    brands = list(brand_list.values())
    brand_dict = {}
    for brand in brands:
        tmp_brand = car_brand_utils.get_carbrand_by_id(
            car_brand_id=brand['id']
        )
        brand_dict[brand['id']] = {
            'brand': tmp_brand,
            'series_list': []
        }
    series_list = list(list_objs(model=ModelName.T_BASE_CAR_SERIES,
                                 orderby=['car_series_cn'],
                                 is_enable=1, is_show=1).values())
    for series in series_list:
        key = series['car_brand_id']
        if key in brand_dict:
            tmp_series = car_series_utils.get_carseries_by_id(
                car_series_id=series['id']
            )
            brand_dict[key]['series_list'].append(tmp_series)
    result_list = []
    for brand_id in brand_ids:
        if brand_id in brand_dict:
            result_list.append(brand_dict[brand_id])
    return result_list

@redis_func()
def get_finance_car_type_dealer(city_id=None, county_id=None, car_type_id=None,
                                per_page=10, page=1):
    """
        任性贷车型页面，PC和WAP通用
        根据城市ID、县区ID和车型ID返回车型的经销商和报价
        排序按 堡垒店-》价格
        如果当前城市没有经销商，就返回最近的售全省的经销商的报价

        参数
        ----
        city_id : int
            城市ID
        county_id : int, 可选
            县区ID
        car_type_id : int
            车型ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            返回车型的经销商和报价
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    car_type_id = common_utils.to_int(car_type_id)

    car_type = car_type_utils.get_cartype_by_id(car_type_id=car_type_id)
    if not car_type:
        return None

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        county_id=county_id,
        car_series_id=car_type['car_series_id']
    )
    if not dealer_id_list:
        return None
    result_list = []
    for dealer_id in dealer_id_list:
        tmp_dealer = dealer_utils.get_dealer_by_id(
            dealer_id=dealer_id
        )
        if not tmp_dealer:
            continue
        tmp_offer_price = offer_price_utils.get_offerprice(
            car_type_id=car_type_id,
            dealer_id=dealer_id
        )
        car_type_dict = {
            'dealer': tmp_dealer,
            'offer_price': tmp_offer_price,
        }
        result_list.append(car_type_dict)
    if result_list:
        result_list = sorted(
            result_list,
            key=lambda tmp_car_type: (
                -tmp_car_type['dealer']['is_vip'],
                tmp_car_type['offer_price']['public_offer_price']
            )
        )
        result_list = result_list[offset: (offset+count)]
    return result_list


@redis_func()
def get_finance_car_series_car_type(city_id=None, car_series_id=None,
                                    car_type_id=None):
    """
        PC端任性贷金融产品列表页
        根据城市ID和车系ID返回对应的车型，car_series_id和car_type_id最少传一个

        参数
        ----
        city_id : int
            城市ID
        car_series_id : int, 可选
            车系ID
        car_type_id : int, 可选
            车型ID

        返回值
        ------
        result_list : list
            返回车系的所有车型的基本数据
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)
    car_type_id = common_utils.to_int(car_type_id)
    if not car_series_id:
        if car_type_id:
            car_type = car_type_utils.get_cartype_by_id(
                car_type_id=car_type_id
            )
            car_series_id = car_type['car_series_id']

    car_type_id_list = car_type_utils.get_cartype_id_list_by_series(
        car_series_id=car_series_id
    )
    if not car_type_id_list:
        return None
    result_list = []
    for tmp_car_type_id in car_type_id_list:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=tmp_car_type_id
        )
        if not tmp_car_type:
            continue
        result_list.append(tmp_car_type)
    if result_list:
        result_list = sorted(
            result_list,
            key=lambda tmp_car_type_info: (tmp_car_type_info['name'])
        )
    return result_list

@redis_func()
def get_finance_car_series_and_car_type(city_id=None, car_series_id=None):
    """
        PC端任性贷金融产品列表页
        根据城市ID和车系ID返回对应的车系的基本数据和所有车型基本数据

        参数
        ----
        city_id : int
            城市ID
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            返回车系的基本数据和所有车型的基本数据
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)

    car_type_id_list = car_type_utils.get_cartype_id_list_by_series(
        car_series_id=car_series_id
    )
    if not car_type_id_list:
        return None
    car_type_list = []
    for tmp_car_type_id in car_type_id_list:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=tmp_car_type_id
        )
        if not tmp_car_type:
            continue
        car_type_list.append(tmp_car_type)
    if car_type_list:
        car_type_list = sorted(
            car_type_list,
            key=lambda tmp_car_type_info: (tmp_car_type_info['name'])
        )
    result_dict = {
        'car_type_list': car_type_list,
        'series': car_series_utils.get_carseries_by_id(
            car_series_id=car_series_id
        )
    }
    return result_dict

@redis_func()
def get_finance_car_series_province_info(car_series_id=None):
    """
        根据车系ID返回销售对应车系的经销商所在的每个省的经销商数量和信息

        参数
        ----
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            返回每个省的经销商数量和信息，还有所有符合条件的经销商总数
    """
    car_series_id = common_utils.to_int(car_series_id)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        car_series_id=car_series_id
    )
    if not dealer_id_list:
        return None
    price_sql_template = '''
        SELECT 
            b.province_id AS province_id, b.province_name, 
            count(a.id) AS dealer_count
        FROM 
            t_base_dealer AS a,
            t_base_province AS b
        WHERE 
            a.id in ({{dealer_id_list}})
            AND a.province_id=b.province_id
            AND a.is_enable=1
            AND a.is_frozen=0
            AND b.is_enable=1
            AND b.is_show=1
        GROUP BY
            a.province_id
        ORDER BY
            a.province_id
    '''
    price_param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    price_sql = Template(price_sql_template).render(price_param)
    cursor = connection().cursor()
    cursor.execute(price_sql, price_param)
    province_list = dictfetchall(cursor)
    if not province_list:
        return None
    result_dict = {
        'province_list': province_list,
    }
    province_count = 0
    for province in province_list:
        province_count += province['dealer_count']
    result_dict['province_count'] = province_count
    return result_dict


@redis_func()
def get_finance_car_series_city_info(province_id=None, car_series_id=None):
    """
        根据省ID和车系ID返回销售对应车系的经销商所在的
        每个城市的经销商数量和信息

        参数
        ----
        province_id : int
            省ID
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            返回每个城市的经销商数量和信息，还有所有符合条件的经销商总数
    """
    province_id = common_utils.to_int(province_id)
    car_series_id = common_utils.to_int(car_series_id)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        province_id=province_id,
        car_series_id=car_series_id
    )
    if not dealer_id_list:
        return None
    price_sql_template = '''
        SELECT 
            b.city_id AS city_id, b.city_name, 
            count(a.id) AS dealer_count
        FROM 
            t_base_dealer AS a,
            t_base_city AS b
        WHERE 
            a.id in ({{dealer_id_list}})
            AND a.city_id=b.city_id
            AND a.is_enable=1
            AND a.is_frozen=0
            AND b.is_enable=1
            AND b.is_show=1
        GROUP BY
            a.city_id
        ORDER BY
            a.city_id
    '''
    price_param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    price_sql = Template(price_sql_template).render(price_param)
    cursor = connection().cursor()
    cursor.execute(price_sql, price_param)
    city_list = dictfetchall(cursor)
    if not city_list:
        return None
    result_dict = {
        'city_list': city_list,
    }
    city_count = 0
    for city in city_list:
        city_count += city['dealer_count']
    result_dict['city_count'] = city_count
    return result_dict

@redis_func()
def get_finance_car_series_county_info(city_id=None, car_series_id=None):
    """
        根据城市ID和车系ID返回销售对应车系的经销商所在的
        每个县区的经销商数量和信息

        参数
        ----
        city_id : int
            城市ID
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            返回每个县区的经销商数量和信息，还有所有符合条件的经销商总数
    """
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        car_series_id=car_series_id
    )
    if not dealer_id_list:
        return None
    price_sql_template = '''
        SELECT 
            b.county_id AS county_id, b.county_name, 
            count(a.id) AS dealer_count
        FROM 
            t_base_dealer AS a,
            t_base_county AS b
        WHERE 
            a.id in ({{dealer_id_list}})
            AND a.county_id=b.county_id
            AND a.is_enable=1
            AND a.is_frozen=0
            AND b.is_enable=1
            AND b.is_show=1
        GROUP BY
            a.county_id
        ORDER BY
            a.county_id
    '''
    price_param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    price_sql = Template(price_sql_template).render(price_param)
    cursor = connection().cursor()
    cursor.execute(price_sql, price_param)
    county_list = dictfetchall(cursor)
    if not county_list:
        return None
    result_dict = {
        'county_list': county_list,
    }
    county_count = 0
    for county in county_list:
        county_count += county['dealer_count']
    result_dict['county_count'] = county_count
    return result_dict


@redis_func()
def get_finance_car_series_list(dealer_id=None):
    """
        通过经销商ID获取经销商当前在售车系

        参数
        ----
        dealer_id : int
            经销商ID

        返回值
        ------
        result_list : list
            返回在售车系数组
    """
    dealer_id = common_utils.to_int(dealer_id)
    dealer = dealer_utils.get_dealer_by_id(dealer_id=dealer_id)
    car_series_id_list = dealer['car_series_ids']
    if not car_series_id_list:
        return None
    result_list = []
    for car_series_id in car_series_id_list:
        car_series = car_series_utils.get_carseries_by_id(
            car_series_id=car_series_id
        )
        if not car_series:
            continue
        result_list.append(car_series)
    if result_list:
        result_list = sorted(
            result_list,
            key=lambda tmp_car_series: (
                common_utils.to_int(tmp_car_series['start_guideprice']),
            )
        )
    return result_list

@redis_func()
def get_finance_city_brand_dealer(city_id=None, car_brand_id=None,
                                  per_page=10, page=1):
    """
        根据城市ID和品牌ID返回经销商信息
        先按VIP排序再按评分排序

        参数
        ----
        city_id : int
            城市ID
        car_brand_id : int
            品牌ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            返回经销商数组
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    car_brand_id = common_utils.to_int(car_brand_id)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        car_brand_id=car_brand_id
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
            %(offset)s, %(count)s
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
        'offset': offset,
        'count': count,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    result_list = []
    for dealer in dealers:
        dealer = dealer_utils.get_dealer_by_id(
            dealer_id=dealer['id']
        )
        result_list.append(dealer)
    return result_list

@redis_func()
def get_finance_county_brand_dealer(county_id=None, car_brand_id=None,
                                    per_page=10, page=1):
    """
        根据县区ID和品牌ID返回经销商信息
        先按VIP排序再按评分排序

        参数
        ----
        county_id : int
            县区ID
        car_brand_id : int
            品牌ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            返回经销商数组
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    county_id = common_utils.to_int(county_id)
    car_brand_id = common_utils.to_int(car_brand_id)

    dealer_id_list = dealer_utils.get_dealer_id_list(
        county_id=county_id,
        car_brand_id=car_brand_id
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
            %(offset)s, %(count)s
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
        'offset': offset,
        'count': count,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    result_list = []
    for dealer in dealers:
        dealer = dealer_utils.get_dealer_by_id(
            dealer_id=dealer['id']
        )
        result_list.append(dealer)
    return result_list

@redis_func()
def get_finance_group_series_car_types(car_series_id=None,
                                       property_key='pailiang'):
    """
        根据车系ID获取所有车型，然后根据property_key属性进行分组排序，
        并返回经销商报价

        参数
        ----
        car_series_id : int
            车系ID
        property_key : str
            车系下的车型按什么属性分组，例如'pailiang'按排量分组

        返回值
        ------
        result_list : list
            返回车系下所有排序好的车型
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
        if not tmp_car_type:
            continue
        tmp_offer_price = offer_price_utils.get_offerprice(
            car_type_id=car_type.id
        )
        tmp_car_type['offer_price'] = tmp_offer_price
        car_type_dict[car_type.id] = tmp_car_type
    car_dict = {}
    for car_prop in car_props:
        key = car_prop.property_value
        if key in car_dict:
            if car_prop.car_type_id in car_type_dict:
                car_dict[key].append(car_type_dict[car_prop.car_type_id])
        else:
            car_dict[key] = []
            if car_prop.car_type_id in car_type_dict:
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
def get_finance_dealer_car_types_price(dealer_id=None, car_type_id=None):
    """
        根据经销商ID和车型ID返回报价

        参数
        ----
        dealer_id : int
            经销商ID
        car_type_id : int
            车型ID

        返回值
        ------
        result_dict : dict
            返回报价
    """
    dealer_id = common_utils.to_int(dealer_id)
    car_type_id = common_utils.to_int(car_type_id)
    offer_price = offer_price_utils.get_offerprice(
        dealer_id=dealer_id,
        car_type_id=car_type_id
    )
    return offer_price

@redis_func()
def get_finance_province_city_county(province_id=None,
                                     city_id=None,
                                     county_id=None):
    """
        根据城市ID或者县区ID返回省和城市信息
        province_id, city_id, county_id都是可选，最少有一个

        参数
        ----
        province_id : int, 可选
            省ID
        city_id : int, 可选
            城市ID
        county_id : int, 可选
            县区ID

        返回值
        ------
        result_dict : dict
            返回省或者城市信息
    """
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    province_id = common_utils.to_int(province_id)
    result_dict = {}
    if county_id:
        county_info = place_utils.get_county_by_id(county_id=county_id)
        if not county_info:
            return None
        city_id = county_info['city_id']
        result_dict['county'] = county_info
    if city_id:
        city_info = place_utils.get_city_by_id(city_id=city_id)
        if not city_info:
            return None
        province_id = city_info['province_id']
        result_dict['city'] = city_info
    if province_id:
        province_info = place_utils.get_province_by_id(province_id=province_id)
        if not province_info:
            return None
        result_dict['province'] = province_info
    return result_dict

@redis_func()
def get_finance_all_province():
    """
        获取所有省的数据

        参数
        ----
        None : None
            空

        返回值
        ------
        result_list : list
            所有省的数据的数组
    """
    province_list = list_objs(model=ModelName.T_BASE_PROVINCE,
                              is_enable=1, is_show=1)
    if not province_list:
        return None
    result_list = []
    for province in province_list:
        province_info = place_utils.get_province_by_id(
            province_id=province.province_id
        )
        if province_info:
            result_list.append(province_info)
    return result_list

@redis_func()
def get_finance_all_city(province_id=None):
    """
        通过省ID获取城市的数据

        参数
        ----
        province_id : int
            省ID

        返回值
        ------
        result_list : list
            所有城市的数据的数组
    """
    province_id = common_utils.to_int(province_id)
    city_list = list_objs(model=ModelName.T_BASE_CITY,
                          is_enable=1, is_show=1,
                          province_id=province_id)
    if not city_list:
        return None
    result_list = []
    for city in city_list:
        city_info = place_utils.get_city_by_id(city_id=city.city_id)
        if city_info:
            result_list.append(city_info)
    return result_list

@redis_func()
def get_finance_all_county(city_id=None):
    """
        通过城市ID获取县区的数据

        参数
        ----
        city_id : int
            城市ID

        返回值
        ------
        result_list : list
            所有县区的数据的数组
    """
    city_id = common_utils.to_int(city_id)
    county_list = list_objs(model=ModelName.T_BASE_COUNTY,
                            is_enable=1, is_show=1,
                            city_id=city_id)
    if not county_list:
        return None
    result_list = []
    for county in county_list:
        county_info = place_utils.get_county_by_id(county_id=county.county_id)
        if county_info:
            result_list.append(county_info)
    return result_list

@redis_func()
def get_finance_dealer_province():
    """
        获取所有包含经销商的省的数据
        
        参数
        ----
        None : None
            空

        返回值
        ------
        result_list : list
            所有省的数据的数组
    """
    dealer_sql_template = '''
        SELECT 
            DISTINCT province_id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
        ORDER BY 
            province_id
    '''
    param = {
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    if not dealers:
        return None
    result_list = []
    for dealer in dealers:
        province_info = place_utils.get_province_by_id(
            province_id=dealer['province_id']
        )
        if province_info:
            result_list.append(province_info)
    return result_list

@redis_func()
def get_finance_dealer_city(province_id=None):
    """
        通过省ID获取所有包含经销商的城市的数据

        参数
        ----
        province_id : int
            省ID

        返回值
        ------
        result_list : list
            所有城市的数据的数组
    """
    province_id = common_utils.to_int(province_id)
    dealer_id_list = dealer_utils.get_dealer_id_list(
        province_id=province_id
    )
    if not dealer_id_list:
        return None

    dealer_sql_template = '''
        SELECT 
            DISTINCT city_id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            AND id in ({{dealer_id_list}})
        ORDER BY 
            city_id
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    if not dealers:
        return None
    result_list = []
    for dealer in dealers:
        city_info = place_utils.get_city_by_id(
            city_id=dealer['city_id']
        )
        if city_info:
            result_list.append(city_info)
    return result_list


@redis_func()
def get_finance_dealer_county(city_id=None):
    """
        通过城市ID获取所有包含经销商的县区的数据

        参数
        ----
        city_id : int
            城市ID

        返回值
        ------
        result_list : list
            所有县区的数据的数组
    """
    city_id = common_utils.to_int(city_id)
    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id
    )
    if not dealer_id_list:
        return None

    dealer_sql_template = '''
        SELECT 
            DISTINCT county_id
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            AND id in ({{dealer_id_list}})
        ORDER BY 
            county_id
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    if not dealers:
        return None
    result_list = []
    for dealer in dealers:
        county_info = place_utils.get_county_by_id(
            county_id=dealer['county_id']
        )
        if county_info:
            result_list.append(county_info)
    return result_list

