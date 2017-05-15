# -*- coding: utf-8 -*-


from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName

from cbbweb.service import get_object
from cbbweb.service.cms_utils import common_utils

@redis_func()
def get_carbrand_by_id(car_brand_id=None):
    """
        根据品牌ID返回品牌实例
    """
    car_brand_id = common_utils.to_int(car_brand_id)
    car_brand = get_object(model=ModelName.T_BASE_CAR_BRAND,
                           is_enable=1, is_show=1,
                           id=car_brand_id)
    if not car_brand:
        return None
    car_brand_dict = {
        'id': car_brand.id,
        'name': car_brand.car_brand_cn,
        'img': car_brand.logo_img,
        'car_brand_en': car_brand.car_brand_en,
        'car_brand_alias': car_brand.car_brand_alias,
        'order_no': car_brand.order_no,
    }
    return car_brand_dict

