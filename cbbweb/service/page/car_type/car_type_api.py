# -*- coding: utf-8 -*-


from jinja2 import Template

from cbbweb.core.utils import str2array
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.db import connection
from cbbweb.core.utils.db import dictfetchall

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_brand_utils
from cbbweb.service.cms_utils import car_series_utils
from cbbweb.service.cms_utils import car_type_utils
from cbbweb.service.cms_utils import offer_price_utils
from cbbweb.service.cms_utils import activity_utils
from cbbweb.service.cms_utils import dealer_utils

@redis_func()
def get_car_type_by_id(car_type_id=None):
    """
        根据车型ID返回车型基本信息

        参数
        ----
        car_type_id : int
            车型ID

        返回值
        ------
        result_dict : dict
            返回车型基本信息
    """
    car_type_id = common_utils.to_int(car_type_id)
    car_type = car_type_utils.get_cartype_by_id(car_type_id=car_type_id)
    return car_type

@redis_func()
def get_car_type_data(city_id=None, car_type_id=None):
    """
        车型页面，PC和WAP通用，
        根据城市ID和车型ID获取车型数据，最低报价

        参数
        ----
        city_id : int
            城市ID
        car_type_id : int
            车型ID

        返回值
        ------
        result_dict : dict
            返回车型数据，最低报价，如果没有经销商报价就用官方指导价
    """
    city_id = common_utils.to_int(city_id)
    car_type_id = common_utils.to_int(car_type_id)
    car_type = car_type_utils.get_cartype_by_id(car_type_id=car_type_id)
    if not car_type:
        return None
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_type['car_series_id']
    )
    if not car_series:
        return None
    car_brand = car_brand_utils.get_carbrand_by_id(
        car_brand_id=car_series['car_brand_id']
    )
    if not car_brand:
        return None
    result_dict = {
        'brand': car_brand,
        'series': car_series,
        'type': car_type,
    }

    offer_price = offer_price_utils.get_offerprice(
        city_id=city_id,
        car_type_id=car_type_id
    )
    result_dict['type']['offer_price'] = offer_price
    return result_dict


@redis_func()
def get_car_type_property_back(car_type_id=None, prop_keys=None):
    """
        车型页面，PC和WAP通用，
        获取车型属性

        参数
        ----
        car_type_id : int
            车型ID
        prop_keys : list of str
            属性对应的字符串数组，例如['pailiang', 'chang']

        返回值
        ------
        result_dict : dict
            返回车型属性
    """
    if not prop_keys:
        return None

    car_type_id = common_utils.to_int(car_type_id)
    prop_keys = str2array(prop_keys)

    cursor = connection().cursor()
    car_type_sql = """
        SELECT 
            a.order_no, a.property_key, a.name, b.property_value 
        FROM 
            t_base_car_type_property_template AS a, 
            t_base_car_type_property AS b 
        WHERE 
            a.id=b.property_id 
            AND b.car_type_id=%s 
            AND a.property_key in %s
            AND a.is_enable=1
            AND b.is_enable=1
    """
    cursor.execute(car_type_sql, [car_type_id, prop_keys])
    rows = dictfetchall(cursor)
    prop_dict = {}
    # for tmp_prop_key in prop_keys:
    #     prop_dict[tmp_prop_key] = {
    #         'order_no': 0,
    #         'property_key': tmp_prop_key,
    #         'name': '',
    #         'property_value': '',
    #     }
    for row in rows:
        prop_dict[row['property_key']] = row
    return prop_dict

@redis_func()
def get_car_type_group_property_back(car_type_id=None, group_key='jibencanshu'):
    """
        车型页面，PC和WAP通用
        获取车型一组属性
        属性组别名是parent_id=0的属性

        参数
        ----
        car_type_id : int
            车型ID
        group_key : str
            属性组对应的字符串'jibencanshu'

        返回值
        ------
        result_list : list
            返回车型属性数组
    """
    car_type_id = common_utils.to_int(car_type_id)
    group = get_object(model=ModelName.T_BASE_CAR_TYPE_PROPERTY_TEMPLATE,
                       is_enable=1,
                       property_key=group_key)
    if not group:
        return None
    group_id = group.id
    cursor = connection().cursor()
    car_type_sql = """
        SELECT 
            a.order_no, a.property_key, a.name, b.property_value 
        FROM 
            t_base_car_type_property_template AS a, 
            t_base_car_type_property AS b 
        WHERE 
            a.id=b.property_id 
            AND b.car_type_id=%s 
            AND a.parent_id=%s
            AND a.is_enable=1
            AND b.is_enable=1
        ORDER BY 
            a.order_no, a.id
    """
    cursor.execute(car_type_sql, [car_type_id, group_id])
    rows = dictfetchall(cursor)
    return rows

@redis_func()
def get_car_type_all_property_back(car_type_id=None):
    """
        车型页面，PC和WAP通用
        获取车型所有属性

        参数
        ----
        car_type_id : int
            车型ID

        返回值
        ------
        result_list : list
            返回车型所有属性数组
    """
    car_type_id = common_utils.to_int(car_type_id)
    cursor = connection().cursor()
    cursor.execute(
        """
            SELECT 
                id, property_key, name, order_no
            FROM
                t_base_car_type_property_template
            WHERE
                parent_id=0
                AND is_enable=1
            ORDER BY
                order_no, id
        """
    )
    templates = dictfetchall(cursor)
    if not templates:
        return None
    property_list = []
    for template in templates:
        cursor.execute(
            """
                SELECT 
                    a.order_no, a.property_key, a.name, b.property_value
                FROM
                    t_base_car_type_property_template AS a,
                    t_base_car_type_property AS b
                WHERE
                    a.parent_id=%s
                    AND a.id=b.property_id
                    AND b.car_type_id=%s
                    AND a.is_enable=1
                    AND b.is_enable=1
                ORDER BY
                    a.order_no, a.id
            """,
            [template['id'], car_type_id]
        )
        propertys = dictfetchall(cursor)
        if not propertys:
            continue
        prop_dict = {
            'group_name': template['name'],
            'property_list': propertys
        }
        property_list.append(prop_dict)
    return property_list

@redis_func()
def get_car_type_price_property(city_id=None, car_type_id=None):
    """
        根据城市ID和车型ID获取基本数据、报价和全部参数

        参数
        ----
        city_id : int
            城市ID
        car_type_id : int
            车型ID

        返回值
        ------
        result_list : list
            返回车型基本数据、报价和全部参数
    """
    city_id = common_utils.to_int(city_id)
    car_type_id = common_utils.to_int(car_type_id)
    car_type = car_type_utils.get_cartype_by_id(
        car_type_id=car_type_id
    )
    if not car_type:
        return None

    offer_price = offer_price_utils.get_offerprice(
        city_id=city_id,
        car_type_id=car_type_id
    )
    car_type['offer_price'] = offer_price
    car_type['property'] = get_car_type_all_property(car_type_id)
    return car_type

@redis_func()
def get_car_type_series_price_property(city_id=None, car_type_id=None):
    """
        根据车型ID获取对应车系基本数据
        和对应车系下所有车型的基本数据、报价和全部参数

        参数
        ----
        city_id : int
            城市ID
        car_type_id : int
            车型ID

        返回值
        ------
        result_list : list
            对应car_type_id的车型排在car_type_list第一个
    """
    city_id = common_utils.to_int(city_id)
    car_type_id = common_utils.to_int(car_type_id)
    car_type = car_type_utils.get_cartype_by_id(
        car_type_id=car_type_id
    )
    if not car_type:
        return None
    car_series_id = car_type['car_series_id']
    car_series = car_series_utils.get_carseries_by_id(
        car_series_id=car_series_id
    )
    if not car_series:
        return None
    result_dict = {
        'series': car_series,
        'car_type_list': []
    }
    ctpp = get_car_type_price_property(city_id, car_type_id)
    result_dict['car_type_list'].append(ctpp)
    car_type_info_list = list_objs(
        model=ModelName.T_BASE_CAR_TYPE,
        orderby=['guide_price'],
        is_enable=1, is_show=1,
        car_series_id=car_series_id
    ).exclude(id=car_type_id)
    for car_type_info in car_type_info_list:
        tmp_ctpp = get_car_type_price_property(city_id, car_type_info.id)
        result_dict['car_type_list'].append(tmp_ctpp)
    return result_dict

@redis_func()
def get_car_type_dealer(city_id=None, county_id=None, car_type_id=None,
                        per_page=10, page=1,
                        orderby='price', descending=False):
    """
        车型页面，PC和WAP通用
        返回对应城市ID、县区ID和车型ID的经销商

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
        orderby : {'price', 'discount'}
            price按报价排序，discount按优惠排序
        descending : {0, 1}
            0按升序，1按降序

        返回值
        ------
        result_list : list
            返回对应城市、县区和车型的经销商
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    car_type_id = common_utils.to_int(car_type_id)
    orderby_price = True
    if orderby == 'discount':
        orderby_price = False
    else:
        orderby_price = True
    if descending:
        if isinstance(descending, str) and (descending.upper() != 'TRUE'):
            descending = False

    car_type = car_type_utils.get_cartype_by_id(car_type_id=car_type_id)
    if not car_type:
        return None
    car_series_id = car_type['car_series_id']

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
        offer_price = offer_price_utils.get_offerprice(
            car_type_id=car_type_id,
            dealer_id=dealer_id
        )
        tmp_dealer['offer_price'] = offer_price

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
def get_city_car_type_dealer_count(city_id=None, car_type_id=None):
    """
        PC端车型页面
        返回对应城市ID和车型ID在各个县区的经销商的数量

        参数
        ----
        city_id : int
            城市ID
        car_type_id : int
            车型ID

        返回值
        ------
        result_list : list
            返回县区的ID，名字和各个县区的经销商数量
    """
    city_id = common_utils.to_int(city_id)
    car_type_id = common_utils.to_int(car_type_id)

    car_type = car_type_utils.get_cartype_by_id(car_type_id=car_type_id)
    if not car_type:
        return None

    dealer_id_list = dealer_utils.get_dealer_id_list(
        city_id=city_id,
        car_series_id=car_type['car_series_id']
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
            a.county_id=b.county_id
            AND a.is_enable=1
            AND a.is_frozen=0
            AND b.is_enable=1
            AND b.is_show=1
            AND a.id in ({{dealer_id_list}})
        GROUP BY
            a.county_id
    '''
    price_param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
    }
    price_sql = Template(price_sql_template).render(price_param)
    cursor = connection().cursor()
    cursor.execute(price_sql, price_param)
    price_list = dictfetchall(cursor)
    if not price_list:
        return None

    return price_list


@redis_func()
def get_car_types_by_car_series_id(car_series_id=None):
    """
        通过车系ID返回对应的车型数据

        参数
        ----
        car_series_id : int
            车系ID

        返回值
        ------
        result_list : list
            返回对应车系的而所有车型的基本数据
    """
    car_series_id = common_utils.to_int(car_series_id)
    car_types = list_objs(model=ModelName.T_BASE_CAR_TYPE,
                          orderby=['guide_price'],
                          is_enable=1, is_show=1,
                          car_series_id=car_series_id)
    if not car_types:
        return []
    result_list = []
    for car_type in car_types:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=car_type.id
        )
        result_list.append(tmp_car_type)
        
    return result_list

@redis_func()
def get_car_type_property(car_type_id=None, prop_keys=None):

    """
        车型页面，PC和WAP通用，
        获取车型属性

        参数
        ----
        car_type_id : int
            车型ID
        prop_keys : list of str
            属性对应的字符串数组，例如['pailiang', 'chang']

        返回值
        ------
        result_dict : dict
            返回车型属性
    """
    if not prop_keys:
        return None

    car_type_id = common_utils.to_int(car_type_id)
    prop_keys = str2array(prop_keys)

    cursor = connection().cursor()
    car_type_sql = """
        SELECT 
            a.order_no, a.property_key, a.name, b.property_value 
        FROM 
            t_base_car_type_property_template AS a, 
            t_base_car_type_property AS b 
        WHERE 
            a.id=b.property_id 
            AND b.car_type_id=%s 
            AND a.property_key in %s
            AND a.is_enable=1
            AND b.is_enable=1
    """
    cursor.execute(car_type_sql, [car_type_id, prop_keys])
    rows = dictfetchall(cursor)
    prop_dict = {}
    for tmp_prop_key in prop_keys:
        prop_dict[tmp_prop_key] = {
            'order_no': 0,
            'property_key': tmp_prop_key,
            'name': '',
            'property_value': '',
        }
    for row in rows:
        prop_dict[row['property_key']] = row
    return prop_dict



@redis_func()
def get_car_type_group_property(car_type_id=None, group_key='jibencanshu'):
    """
        车型页面，PC和WAP通用
        获取车型一组属性
        属性组别名是parent_id=0的属性

        参数
        ----
        car_type_id : int
            车型ID
        group_key : str
            属性组对应的字符串'jibencanshu'

        返回值
        ------
        result_list : list
            返回车型属性数组
    """
    car_type_id = common_utils.to_int(car_type_id)
    group = get_object(model=ModelName.T_BASE_CAR_TYPE_PROPERTY_TEMPLATE,
                       is_enable=1, parent_id=0,
                       property_key=group_key)


    if not group:
        return None
    group_id = group.id

    cursor = connection().cursor()
    rows = []
    get_pid_sql = '''
        SELECT 
            id,order_no,name,property_key
        FROM
            t_base_car_type_property_template
        WHERE
            parent_id = %s
            AND is_enable=1
        ORDER BY 
            order_no,id
    '''

    cursor.execute(get_pid_sql, group_id)
    exist_pid = dictfetchall(cursor)

    id_list = []
    for one_pid in exist_pid:
        id_list.append(one_pid['id'])

    car_type_sql = """
        SELECT 
            property_value,property_id
        FROM  
            t_base_car_type_property
        WHERE 
            car_type_id=%s
            AND property_id in %s 
            AND is_enable=1
    """
    cursor.execute(car_type_sql, (car_type_id, id_list))
    exist_value = dictfetchall(cursor)

    tmp_dict = {}
    for tmp_info in exist_value:
        tmp_dict[tmp_info['property_id']] = tmp_info

    tmp_list = []
    for pid_son in exist_pid:
        append_dict = {}
        append_dict['name'] = pid_son['name']
        append_dict['order_no'] = pid_son['order_no']
        if pid_son['id'] in tmp_dict:
            append_dict['property_value'] = tmp_dict[pid_son['id']]['property_value']
        else:
            append_dict['property_value'] = ''
        append_dict['property_key'] = pid_son['property_key']
        tmp_list.append(append_dict)
    rows = tmp_list
    return rows

@redis_func()
def get_car_type_all_property(car_type_id=None):
    """
        车型页面，PC和WAP通用
        获取车型所有属性

        参数
        ----
        car_type_id : int
            车型ID

        返回值
        ------
        result_list : list
            返回车型所有属性数组
    """
    car_type_id = common_utils.to_int(car_type_id)
    cursor = connection().cursor()
    cursor.execute(
        """
            SELECT 
                id, property_key, name, order_no
            FROM
                t_base_car_type_property_template
            WHERE
                parent_id=0
                AND is_enable=1
            ORDER BY
                order_no, id
        """
    )
    templates = dictfetchall(cursor)
    if not templates:
        return None
    property_list = []
    for template in templates:
        rows = []
        get_pid_sql = '''
            SELECT 
                id,order_no,name,property_key
            FROM
                t_base_car_type_property_template
            WHERE
                parent_id = %s
                AND is_enable=1
            ORDER BY 
                order_no,id
        '''

        cursor.execute(get_pid_sql, template['id'])
        exist_pid = dictfetchall(cursor)

        id_list = []
        for one_pid in exist_pid:
            id_list.append(one_pid['id'])

        car_type_sql = """
            SELECT 
                property_value,property_id
            FROM  
                t_base_car_type_property
            WHERE 
                car_type_id=%s
                AND property_id in %s 
                AND is_enable=1
        """
        cursor.execute(car_type_sql, (car_type_id, id_list))
        exist_value = dictfetchall(cursor)
        if exist_value:
            tmp_dict = {}
            for tmp_info in exist_value:
                tmp_dict[tmp_info['property_id']] = tmp_info

            tmp_list = []
            for pid_son in exist_pid:
                append_dict = {}
                append_dict['name'] = pid_son['name']
                append_dict['order_no'] = pid_son['order_no']
                if pid_son['id'] in tmp_dict:
                    append_dict['property_value'] = tmp_dict[pid_son['id']]['property_value']
                else:
                    append_dict['property_value'] = ''
                append_dict['property_key'] = pid_son['property_key']
                tmp_list.append(append_dict)
            rows = tmp_list
            prop_dict = {
                'group_name': template['name'],
                'property_list': rows
            }
            property_list.append(prop_dict)

    return property_list
