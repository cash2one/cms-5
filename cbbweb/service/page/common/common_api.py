# -*- coding: utf-8 -*-


from cbbweb.core.utils.rediscache import redis_func

from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import place_utils



@redis_func()
def get_place_province_by_id(province_id=None):
    """
        根据省ID获取省基本数据

        参数
        ----
        province_id : int
            省ID

        返回值
        ------
        result_dict : dict
            省基本数据
    """
    province_id = common_utils.to_int(province_id)
    province = place_utils.get_province_by_id(province_id=province_id)
    return province

@redis_func()
def get_place_city_by_id(city_id=None):
    """
        根据市ID获取市基本数据

        参数
        ----
        city_id : int
            市ID

        返回值
        ------
        result_dict : dict
            市基本数据
    """
    city_id = common_utils.to_int(city_id)
    city = place_utils.get_city_by_id(city_id=city_id)
    return city

@redis_func()
def get_place_county_by_id(county_id=None):
    """
        根据县区ID获取县区基本数据

        参数
        ----
        city_id : int
            县区ID

        返回值
        ------
        result_dict : dict
            县区基本数据
    """
    county_id = common_utils.to_int(county_id)
    county = place_utils.get_county_by_id(county_id=county_id)
    return county









