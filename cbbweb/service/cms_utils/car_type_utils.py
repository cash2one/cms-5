# -*- coding: utf-8 -*-



from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.db import connection
from cbbweb.core.utils.db import dictfetchall

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.catalogs_service import get_car_type_url
from cbbweb.service.product_service import get_product_images
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_series_utils


@redis_func()
def offer_price_section(guide_price, tmp_offer_price_section):
    """
        安全报价区间开始
    """
    if tmp_offer_price_section:
        price_str_list = tmp_offer_price_section.split('-')
        if len(price_str_list) == 2:
            try:
                price_start = int(price_str_list[0])
                price_end = int(price_str_list[1])
                return (price_start, price_end)
            except Exception as err_exc:
                print(str(err_exc))
                if guide_price:
                    return (guide_price, guide_price)
    if guide_price:
        return (guide_price, guide_price)
    else:
        return (0, 0)

@redis_func()
def color_code(tmp_color_code):
    """
        外观颜色编码
        颜色类型（1-外观，2-内饰）
    """
    if not tmp_color_code:
        return []
    color_code_list = tmp_color_code.split(',')
    prop_list = list_objs(model=ModelName.T_BASE_CAR_COLOR,
                          orderby=['order_no'],
                          is_enable=1,
                          is_show=1,
                          color_type=1,
                          id__in=color_code_list)
    prop_list = list(prop_list.values('color_name', 'rgb_value'))
    return prop_list

@redis_func()
def incolor_code(tmp_incolor_code):
    """
        内饰颜色编码
        颜色类型（1-外观，2-内饰）
    """
    if not tmp_incolor_code:
        return []
    incolor_code_list = tmp_incolor_code.split(',')
    prop_list = list_objs(model=ModelName.T_BASE_CAR_COLOR,
                          orderby=['order_no'],
                          is_enable=1,
                          is_show=1,
                          color_type=2,
                          id__in=incolor_code_list)
    prop_list = list(prop_list.values('color_name', 'rgb_value'))
    return prop_list

@redis_func()
def quality_assurance(tmp_quality_assurance):
    """
        整车质保
    """
    if not tmp_quality_assurance:
        return ""
    dict_group = get_object(model=ModelName.T_BASE_DATA_DICT_GROUP,
                            is_enable=1, is_show=1,
                            dictgroup_name='qualityAssurance')
    if not dict_group:
        return ""
    dict_group_id = dict_group.id
    prop = get_object(model=ModelName.T_BASE_DATA_DICT,
                      is_enable=1, is_show=1,
                      dictgroup_id=dict_group_id,
                      dict_key=tmp_quality_assurance)
    if not prop:
        return ""
    return prop.dict_value

@redis_func()
def characteristic_activity(tmp_characteristic_activity):
    """
        特色活动
    """
    if not tmp_characteristic_activity:
        return []
    dict_group = get_object(model=ModelName.T_BASE_DATA_DICT_GROUP,
                            is_enable=1, is_show=1,
                            dictgroup_name='charactActivity')
    if not dict_group:
        return []
    dict_group_id = dict_group.id
    activity_list = tmp_characteristic_activity.split(',')
    prop_list = []
    for activity_key in activity_list:
        if activity_key:
            prop = get_object(model=ModelName.T_BASE_DATA_DICT,
                              is_enable=1, is_show=1,
                              dictgroup_id=dict_group_id,
                              dict_key=activity_key)
            prop_list.append(prop.dict_value)
        else:
            prop_list.append(None)
    return prop_list

@redis_func()
def product_spot(tmp_product_spot):
    """
        产品亮点
    """
    if not tmp_product_spot:
        return []
    spot_list = tmp_product_spot.split(',')
    result_list = []
    for spot in spot_list:
        if spot.strip():
            result_list.append(spot)
    return result_list

@redis_func()
def get_cartype_by_id(car_type_id=None):
    """
        根据车型ID返回车型实例
    """
    car_type_id = common_utils.to_int(car_type_id)
    car_type = get_object(model=ModelName.T_BASE_CAR_TYPE, 
                          is_enable=1, is_show=1, id=car_type_id)
    if not car_type:
        return None
    car_series = get_object(model=ModelName.T_BASE_CAR_SERIES,
                            is_enable=1, is_show=1,
                            id=car_type.car_series_id)
    if not car_series:
        return None
    guide_price = common_utils.to_int(car_type.guide_price)
    (offer_price_start, offer_price_end) = offer_price_section(
        guide_price, car_type.offer_price_section
    )
    car_type_dict = {
        'id': car_type.id,
        'url': get_car_type_url(car_series.id, car_type.id),
        'name': car_type.car_type_name,
        'car_brand_id': car_type.car_brand_id,
        'car_series_id': car_type.car_series_id,
        'guide_price': car_type.guide_price,
        'offer_price_section': car_type.offer_price_section,
        'offer_price_start': offer_price_start,
        'offer_price_end': offer_price_end,
        'color_code': color_code(car_type.color_code),
        'incolor_code': incolor_code(car_type.incolor_code),
        'quality_assurance': quality_assurance(car_type.quality_assurance),
        'characteristic_activity': characteristic_activity(
            car_type.characteristic_activity
        ),
        'product_spot': product_spot(car_type.product_spot),
        # 'price': car_type.guide_price,
        # 'discount': 0,
        # 'guide_price': car_type.guide_price,
        # 'dealer_id': None,
        
        # 'imgs': get_product_images(series_id=str(car_series.id),
        #                            model_id=str(car_type.id),
        #                            position=1,
        #                            countofpage=5, pagecount=0),
        'imgs': []
    }
    if not car_type_dict['imgs']:
        tmp_car_series = car_series_utils.get_carseries_by_id(
            car_type_dict['car_series_id']
        )
        if tmp_car_series:
            if tmp_car_series['pc_thumbnail']:
                car_type_dict['imgs'] = [
                    {
                        'CDNPATH': tmp_car_series['pc_thumbnail']
                    }
                ]
        # tmp_car_series = get_object(model=ModelName.T_BASE_CAR_SERIES,
        #                             is_enable=1, is_show=1,
        #                             id=car_type_dict['car_series_id'])
        # if tmp_car_series:
        #     if tmp_car_series.pc_thumbnail:
        #         car_type_dict['imgs'] = [
        #             {
        #                 'CDNPATH': tmp_car_series.pc_thumbnail
        #             }
        #         ]
    return car_type_dict

@redis_func()
def get_cartype_id_list_by_series(car_series_id=None):
    """
        根据车系ID返回对应的所有车型的ID数组
    """
    car_series_id = common_utils.to_int(car_series_id)
    car_type_sql = '''
        SELECT 
            id
        FROM 
            t_base_car_type
        WHERE 
            is_enable=1
            AND is_show=1
            AND car_series_id=%(car_series_id)s
    '''
    param = {
        'car_series_id': car_series_id,
    }
    cursor = connection().cursor()
    cursor.execute(car_type_sql, param)
    car_type_list = dictfetchall(cursor)
    if not car_type_list:
        return None
    car_type_id_list = []
    for tmp_car_type in car_type_list:
        car_type_id_list.append(tmp_car_type['id'])
    return car_type_id_list

