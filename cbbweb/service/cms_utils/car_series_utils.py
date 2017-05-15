# -*- coding: utf-8 -*-



from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.catalogs_service import get_car_series_url
# from cbbweb.service.product_service import get_product_images
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_brand_utils


@redis_func()
def car_property(tmp_car_property):
    """
        车系属性（热销，推荐，钜惠，新车，购置税减半）
    """
    if not tmp_car_property:
        return []
    dict_group = get_object(model=ModelName.T_BASE_DATA_DICT_GROUP,
                            is_enable=1, is_show=1,
                            dictgroup_name='carSeriesProperty')
    if not dict_group:
        return []
    dict_group_id = dict_group.id
    car_prop_list = tmp_car_property.split(',')
    prop_list = list_objs(model=ModelName.T_BASE_DATA_DICT,
                          orderby=['sort_order'],
                          is_enable=1, is_show=1,
                          dictgroup_id=dict_group_id,
                          dict_key__in=car_prop_list)
    prop_list = list(prop_list.values_list('dict_value', flat=True))
    return prop_list

@redis_func()
def car_series_imgs(default_img, multi_angle_img):
    """
        车系图片
    """
    imgs_list = []
    if default_img:
        imgs_list.append(
            {
                'CDNPATH': default_img
            }
        )
    if multi_angle_img:
        mai_list = multi_angle_img.split(',,,')
        for mai in mai_list:
            if mai:
                imgs_list.append(
                    {
                        'CDNPATH': mai
                    }
                )
    return imgs_list

@redis_func()
def get_carseries_by_id(car_series_id=None):
    """
        根据车系ID返回车系实例
    """
    car_series_id = common_utils.to_int(car_series_id)
    car_series = get_object(model=ModelName.T_BASE_CAR_SERIES,
                            is_enable=1, is_show=1, id=car_series_id)
    if not car_series:
        return None
    car_brand = car_brand_utils.get_carbrand_by_id(
        car_brand_id=car_series.car_brand_id
    )
    if not car_brand:
        return None
    car_series_dict = {
        'id': car_series.id,
        'url': get_car_series_url(car_series.id),
        'car_brand_id': car_series.car_brand_id,
        'name': car_series.car_series_cn,
        'highlight': None,
        'car_property': car_property(car_series.car_property),
        'introdution': car_series.brief_introdution,
        'start_guideprice': car_series.start_guideprice,
        'end_guideprice': car_series.end_guideprice,
        'pc_thumbnail': car_series.pc_thumbnail,
        'wap_thumbnail': car_series.pc_thumbnail, # car_series.wap_thumbnail,
        'sales': car_series.sales,
        'order_no': car_series.order_no,
        'imgs': car_series_imgs(car_series.pc_thumbnail,
                                car_series.multi_angle_img),
        # 'imgs': get_product_images(series_id=str(car_series.id),
        #                            position=1,
        #                            countofpage=5, pagecount=0),
        'brand': car_brand,
    }
    return car_series_dict
