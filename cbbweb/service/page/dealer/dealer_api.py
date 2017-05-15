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
from cbbweb.service.cms_utils import car_series_utils
from cbbweb.service.cms_utils import car_type_utils
from cbbweb.service.cms_utils import offer_price_utils
from cbbweb.service.cms_utils import activity_utils
from cbbweb.service.cms_utils import dealer_utils


@redis_func()
def get_dealer_by_id(dealer_id=None):
    """
        根据经销商ID返回经销商数据

        参数
        ----
        dealer_id : int
            经销商ID

        返回值
        ------
        result_dict : dict
            返回经销商的基本数据
    """
    dealer_id = common_utils.to_int(dealer_id)
    return dealer_utils.get_dealer_by_id(dealer_id=dealer_id)


@redis_func()
def get_dealer_by_default(city_id=None, county_id=None,
                          brand_id=None, series_id=None,
                          per_page=10, page=1, newest_activity=None):
    """
        PC端找好店首页
        WAP端找好店首页-默认
        先按VIP排序再按评分排序

        参数
        ----
        city_id : int
            城市ID
        county_id : int, 可选
            县区ID
        brand_id : int, 可选
            品牌ID
        series_id : int, 可选
            车系ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码
        newest_activity : int
            是否返回最新促销活动数组 activity_list，1返回，0不返回。
            会覆盖车系ID对应的促销活动数组 activity_list

        返回值
        ------
        result_dict : dict
            返回当前城市的经销商数量和过滤后的经销商数量和经销商数组
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    brand_id = common_utils.to_int(brand_id)
    series_id = common_utils.to_int(series_id)
    newest_activity = common_utils.to_int(newest_activity)

    dealer_id_list = dealer_utils.get_dealer_id_list(city_id=city_id,
                                                     county_id=county_id,
                                                     car_brand_id=brand_id,
                                                     car_series_id=series_id)
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
    dealer_list = []
    for dealer in dealers:
        dealer = dealer_utils.get_dealer_by_id(
            dealer_id=dealer['id']
        )
        if newest_activity:
            tmp_activity_list = activity_utils.get_activity_list_by_dealer(
                dealer_id=dealer['id'],
                activity_type=1,
            )
            dealer['activity_list'] = tmp_activity_list
        elif series_id:
            activity_list = activity_utils.get_activity_list_by_dealer_series(
                dealer_id=dealer['id'],
                car_series_id=series_id
            )
            dealer['activity_list'] = activity_list
        dealer_list.append(dealer)

    filter_count = len(dealer_id_list)

    # city count
    city_count = dealer_utils.get_dealer_count(city_id=city_id)
    result_dict = {
        'city_count': city_count,
        'filter_count': filter_count,
        'dealer_list': dealer_list,
        'page_count': int((filter_count + count - 1) / count),
    }

    # filter car series
    if series_id:
        result_dict['car_series_list'] = [
            car_series_utils.get_carseries_by_id(car_series_id=series_id)
        ]
    else:
        all_dealer_list = dealer_utils.get_dealer_list_by_id_list(
            dealer_id_list=dealer_id_list
        )
        tmp_dict = {}
        for tmp_dealer in all_dealer_list:
            if tmp_dealer['car_series_ids']:
                for tmp_car_series_id in tmp_dealer['car_series_ids']:
                    tmp_dict[tmp_car_series_id] = 1
        tmp_car_series_id_list = tmp_dict.keys()
        car_series_list = []
        for tmp_car_series_id in tmp_car_series_id_list:
            car_series_info = car_series_utils.get_carseries_by_id(
                car_series_id=tmp_car_series_id
            )
            if car_series_info:
                if brand_id:
                    if car_series_info['car_brand_id'] == brand_id:
                        car_series_list.append(car_series_info)
                else:
                    car_series_list.append(car_series_info)
        if car_series_list:
            car_series_list = sorted(
                car_series_list,
                key=lambda tmp_car_series: tmp_car_series['order_no']
            )
        result_dict['car_series_list'] = car_series_list
    return result_dict

@redis_func()
def get_dealer_by_score(city_id=None, county_id=None,
                        brand_id=None, series_id=None,
                        per_page=10, page=1, newest_activity=None):
    """
        WAP端找好店首页-好评优先
        先按评分排序再按VIP排序

        参数
        ----
        city_id : int
            城市ID
        county_id : int, 可选
            县区ID
        brand_id : int, 可选
            品牌ID
        series_id : int, 可选
            车系ID
        per_page : int
            当前页返回的数据数量
        page : int
            页码
        newest_activity : int
            是否返回最新促销活动数组 activity_list，1返回，0不返回。
            会覆盖车系ID对应的促销活动数组 activity_list

        返回值
        ------
        result_dict : dict
            返回当前城市的经销商数量和过滤后的经销商数量和经销商数组
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    brand_id = common_utils.to_int(brand_id)
    series_id = common_utils.to_int(series_id)
    newest_activity = common_utils.to_int(newest_activity)

    dealer_id_list = dealer_utils.get_dealer_id_list(city_id=city_id,
                                                     county_id=county_id,
                                                     car_brand_id=brand_id,
                                                     car_series_id=series_id)
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
            sales_score desc, is_vip desc
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
    dealer_list = []
    for dealer in dealers:
        dealer = dealer_utils.get_dealer_by_id(dealer_id=dealer['id'])
        if newest_activity:
            tmp_activity_list = activity_utils.get_activity_list_by_dealer(
                dealer_id=dealer['id'],
                activity_type=1,
            )
            dealer['activity_list'] = tmp_activity_list
        elif series_id:
            activity_list = activity_utils.get_activity_list_by_dealer_series(
                dealer_id=dealer['id'],
                car_series_id=series_id
            )
            dealer['activity_list'] = activity_list
        dealer_list.append(dealer)

    filter_count = len(dealer_id_list)

    # city count
    city_count = dealer_utils.get_dealer_count(city_id=city_id)
    result_dict = {
        'city_count': city_count,
        'filter_count': filter_count,
        'dealer_list': dealer_list,
        'page_count': int((filter_count + count - 1) / count),
    }

    return result_dict


@redis_func()
def get_dealer_by_distance(city_id=None, county_id=None,
                           brand_id=None, series_id=None,
                           longitude=None, latitude=None,
                           per_page=10, page=1, newest_activity=None):
    """
        WAP端找好店首页-离我最近
        按经纬度距离排序

        参数
        ----
        city_id : int
            城市ID
        county_id : int, 可选
            县区ID
        brand_id : int, 可选
            品牌ID
        series_id : int, 可选
            车系ID
        longitude : float
            经度
        latitude : float
            纬度
        per_page : int
            当前页返回的数据数量
        page : int
            页码
        newest_activity : int
            是否返回最新促销活动数组 activity_list，1返回，0不返回。
            会覆盖车系ID对应的促销活动数组 activity_list

        返回值
        ------
        result_dict : dict
            返回当前城市的经销商数量和过滤后的经销商数量和经销商数组
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    city_id = common_utils.to_int(city_id)
    county_id = common_utils.to_int(county_id)
    brand_id = common_utils.to_int(brand_id)
    series_id = common_utils.to_int(series_id)
    longitude = common_utils.to_float(longitude)
    latitude = common_utils.to_float(latitude)
    newest_activity = common_utils.to_int(newest_activity)

    dealer_id_list = dealer_utils.get_dealer_id_list(city_id=city_id,
                                                     county_id=county_id,
                                                     car_brand_id=brand_id,
                                                     car_series_id=series_id)
    if not dealer_id_list:
        return None
    dealer_sql_template = '''
        SELECT 
            id,
            (
                (longitude-%(longitude)s)*(longitude-%(longitude)s)
                +(latitude-%(latitude)s)*(latitude-%(latitude)s)
            ) AS dealer_distance
        FROM 
            t_base_dealer
        WHERE 
            is_enable=1
            AND is_frozen=0
            AND id in ({{dealer_id_list}})
        ORDER BY 
            dealer_distance
        LIMIT 
            %(offset)s, %(count)s
    '''
    param = {
        'dealer_id_list': common_utils.int_list_to_str(dealer_id_list),
        'longitude': longitude,
        'latitude': latitude,
        'offset': offset,
        'count': count,
    }
    dealer_sql = Template(dealer_sql_template).render(param)
    cursor = connection().cursor()
    cursor.execute(dealer_sql, param)
    dealers = dictfetchall(cursor)
    dealer_list = []
    for dealer in dealers:
        dealer = dealer_utils.get_dealer_by_id(dealer_id=dealer['id'])
        dealer['distance'] = common_utils.geo_distance(latitude, longitude,
                                                       dealer['latitude'],
                                                       dealer['longitude'])
        if newest_activity:
            tmp_activity_list = activity_utils.get_activity_list_by_dealer(
                dealer_id=dealer['id'],
                activity_type=1,
            )
            dealer['activity_list'] = tmp_activity_list
        elif series_id:
            activity_list = activity_utils.get_activity_list_by_dealer_series(
                dealer_id=dealer['id'],
                car_series_id=series_id
            )
            if activity_list:
                dealer['activity_list'] = activity_list
        dealer_list.append(dealer)

    filter_count = len(dealer_id_list)

    # city count
    city_count = dealer_utils.get_dealer_count(city_id=city_id)
    result_dict = {
        'city_count': city_count,
        'filter_count': filter_count,
        'dealer_list': dealer_list,
        'page_count': int((filter_count + count - 1) / count),
    }

    return result_dict


@redis_func()
def get_dealer_on_sale_car_types(dealer_id=None, car_type=0,
                                 per_page=10, page=1):
    """
        找好店 PC端店铺页|WAP端商家详情页,
        根据经销商ID和官网车型级别查询在售车型

        参数
        ----
        dealer_id : int
            经销商ID
        car_type : {0, 1, 2, 3, 4}
            官网车型级别参数，0为全部，1是三厢，2是两厢，3是SUV，4是进口
        per_page : int
            当前页返回的数据数量
        page : int
            页码

        返回值
        ------
        result_list : list
            返回当前经销商的在售车系和对应的所有车型，根据车型报价排序
    """
    (offset, count) = common_utils.offset_count(per_page=per_page, page=page)
    dealer_id = common_utils.to_int(dealer_id)
    official_car_type = common_utils.to_int(car_type)

    dealer = dealer_utils.get_dealer_by_id(dealer_id)
    if not dealer:
        return None
    sale_series_id_list = dealer['car_series_ids']
    car_series_list = None
    if official_car_type == 0:
        car_series_list = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                                    orderby=['order_no'],
                                    offset=offset, count=count,
                                    is_enable=1, is_show=1,
                                    id__in=sale_series_id_list)
    else:
        car_series_list = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                                    orderby=['order_no'],
                                    offset=offset, count=count,
                                    is_enable=1, is_show=1,
                                    id__in=sale_series_id_list,
                                    official_car_level=official_car_type)
    result_list = []
    for tmp_car_series in car_series_list:
        car_type_id_list = car_type_utils.get_cartype_id_list_by_series(
            car_series_id=tmp_car_series.id
        )
        if not car_type_id_list:
            continue
        car_type_list = []
        for car_type_id in car_type_id_list:
            car_type = car_type_utils.get_cartype_by_id(
                car_type_id=car_type_id
            )
            if not car_type:
                continue
            car_type['offer_price'] = offer_price_utils.get_offerprice(
                dealer_id=dealer_id,
                car_type_id=car_type_id
            )
            car_type_list.append(car_type)
        if car_type_list:
            car_type_list = sorted(
                car_type_list,
                key=lambda tmp_car_type: (
                    tmp_car_type['offer_price']['price']
                )
            )
        activity_list = activity_utils.get_activity_list_by_dealer_series(
            dealer_id=dealer_id,
            car_series_id=tmp_car_series.id
        )
        info_dict = {
            'series': car_series_utils.get_carseries_by_id(
                car_series_id=tmp_car_series.id
            ),
            'type_list': car_type_list,
            'activity_list': activity_list,
        }
        result_list.append(info_dict)
    result_list = sorted(
        result_list,
        key=lambda price: (
            price['type_list'][0]['offer_price']['price'] 
            if price['type_list'] else 0
        )
    )
    return result_list

@redis_func()
def get_dealer_on_sale_car_types_count(dealer_id=None):
    """
        找好店 PC端店铺页|WAP端商家详情页
        经销商在售车型总数

        参数
        ----
        dealer_id : int
            经销商ID

        返回值
        ------
        count : int
            返回经销商在售车型总数
    """
    dealer_id = common_utils.to_int(dealer_id)
    dealer = dealer_utils.get_dealer_by_id(dealer_id)
    if not dealer:
        return None
    sale_series_id_list = dealer['car_series_ids']
    car_type_count = 0
    for car_series_id in sale_series_id_list:
        car_type_id_list = car_type_utils.get_cartype_id_list_by_series(
            car_series_id=car_series_id
        )
        if car_type_id_list:
            car_type_count += len(car_type_id_list)
    return car_type_count


@redis_func()
def get_dealer_group_series_car_types(dealer_id=None, car_series_id=None,
                                      property_key=None):
    """
        找好店店铺页面
        找好店商家详情页
        用在更换车型的列表
        根据车系ID获取所有车型，然后根据property_key属性进行分组排序

        参数
        ----
        dealer_id : int
            经销商ID
        car_series_id : int
            车系ID
        property_key : str
            车系下的车型按什么属性分组，例如'pailiang'按排量分组

        返回值
        ------
        result_list : list
            返回经销商所有车型报价，经销商没有报价的车型用厂家指导价代替
    """
    dealer_id = common_utils.to_int(dealer_id)
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
            dealer_id=dealer_id,
            car_type_id=car_type.id
        )
        tmp_car_type['offer_price'] = tmp_offer_price
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
def get_dealer_activity_series_car_types(dealer_id=None, car_series_id=None):
    """
        WAP端经销商活动页面
        根据经销商ID和车系ID获取所有车型和报价，还有车系的经销商最低价最高价

        参数
        ----
        dealer_id : int
            经销商ID
        car_series_id : int
            车系ID

        返回值
        ------
        result_dict : dict
            返回所有车型和报价，还有车系的经销商最低价最高价
    """
    dealer_id = common_utils.to_int(dealer_id)
    car_series_id = common_utils.to_int(car_series_id)
    car_types = list_objs(model=ModelName.T_BASE_CAR_TYPE,
                          orderby=['guide_price'],
                          is_enable=1, is_show=1,
                          car_series_id=car_series_id)
    if not car_types:
        return None
    car_type_list = []
    car_type_price_min = 99999999
    car_type_price_max = 0
    for car_type in car_types:
        tmp_car_type = car_type_utils.get_cartype_by_id(
            car_type_id=car_type.id
        )
        if not tmp_car_type:
            continue
        tmp_offer_price = offer_price_utils.get_offerprice(
            dealer_id=dealer_id,
            car_type_id=car_type.id
        )
        tmp_car_type['offer_price'] = tmp_offer_price
        car_type_list.append(tmp_car_type)
        # car type price
        if tmp_car_type['offer_price']['price'] < car_type_price_min:
            car_type_price_min = tmp_car_type['offer_price']['price']
        if tmp_car_type['offer_price']['price'] > car_type_price_max:
            car_type_price_max = tmp_car_type['offer_price']['price']
    result_dict = {
        'series': car_series_utils.get_carseries_by_id(
            car_series_id=car_series_id
        ),
        'car_type_list': car_type_list

    }
    activity_list = activity_utils.get_activity_list_by_dealer_series(
        dealer_id=dealer_id,
        car_series_id=car_series_id
    )
    result_dict['series']['activity_list'] = activity_list
    result_dict['series']['car_type_price_min'] = car_type_price_min
    result_dict['series']['car_type_price_max'] = car_type_price_max
    return result_dict

@redis_func()
def get_dealer_car_series_property(car_series_id=None, prop_keys=None):
    """
        PC经销商促销活动
        根据车系ID和属性KEY数组获取车系属性

        参数
        ----
        car_series_id : int
            车系ID
        property_key : str
            车系下的车型按什么属性分组，例如'pailiang'按排量分组

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


@redis_func()
def get_dealer_hot_car_series(count=3):
    """
        热销车系，根据t_base_car_series的sales降序排序

        参数
        ----
        count : int
            获取车系的数量

        返回值
        ------
        result_list : list
            返回排好序的车系数组
    """
    count = common_utils.max_int(count)
    car_series_list = list_objs(model=ModelName.T_BASE_CAR_SERIES,
                                orderby=['-sales'],
                                count=count,
                                is_enable=1, is_show=1)
    if not car_series_list:
        return None
    result_list = []
    for tmp_car_series in car_series_list:
        car_series = car_series_utils.get_carseries_by_id(
            car_series_id=tmp_car_series.id
        )
        if not car_series:
            continue
        result_list.append(car_series)
    return result_list

@redis_func()
def get_dealer_promotion_activity(dealer_id=None, count=5):
    """
        通过经销商ID获取经销商促销活动，按创建时间排序

        参数
        ----
        dealer_id : int
            经销商ID
        count : int
            获取促销活动的数量

        返回值
        ------
        result_list : list
            返回排好序的促销活动数组
    """
    dealer_id = common_utils.to_int(dealer_id)
    count = common_utils.max_int(count)
    activity_ids = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                             is_enable=1,
                             orderby=['-created_date'],
                             count=count,
                             activity_type=1,
                             dealer_id=dealer_id)
    activity_ids = activity_ids.values_list('id', flat=True)
    activity_list = []
    for activity_id in activity_ids:
        tmp_activity = activity_utils.get_activity_by_id(
            activity_id=activity_id
        )
        activity_list.append(tmp_activity)
    return activity_list

@redis_func()
def get_dealer_city_activity(city_id=None, activity_type=1, count=6):
    """
        通过城市ID和活动类型返回同城经销商活动

        参数
        ----
        city_id : int
            城市ID
        activity_type : {1, 2}
            1促销活动，2店头活动
        count : int
            获取活动的数量

        返回值
        ------
        result_list : list
            返回排好序的活动数组
    """
    city_id = common_utils.to_int(city_id)
    activity_type = common_utils.to_int(activity_type)
    count = common_utils.max_int(count)
    activity_ids = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                             is_enable=1,
                             orderby=['-created_date'],
                             count=count,
                             activity_type=activity_type,
                             city_id=city_id)
    activity_ids = activity_ids.values_list('id', flat=True)
    activity_list = []
    for activity_id in activity_ids:
        tmp_activity = activity_utils.get_activity_by_id(
            activity_id=activity_id
        )
        activity_list.append(tmp_activity)
    return activity_list

@redis_func()
def get_dealer_offical_car_info(dealer_id=None):
    """
        找好店 PC端店铺页|WAP端商家详情页,
        根据经销商ID查询在售车系信息，以官网车型级别分类

        参数
        ----
        dealer_id : int
            经销商ID

        返回值
        ------
        result_dict : dict
            返回当前经销商的在售车系，以官网车型级别分类，
            1是三厢车，2是两厢车，3是SUV，4是原装进口
    """
    dealer_id = common_utils.to_int(dealer_id)

    dealer = dealer_utils.get_dealer_by_id(dealer_id)
    if not dealer:
        return None
    sale_series_id_list = dealer['car_series_ids']
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
                                    id__in=sale_series_id_list,
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



