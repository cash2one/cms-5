# -*- coding: utf-8 -*-



from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import get_object



PER_PAGE_MAX = 50


@redis_func()
def get_province_by_id(province_id=None):
    tmp_province = get_object(model=ModelName.T_BASE_PROVINCE,
                              is_enable=1, is_show=1,
                              province_id=province_id)
    if not tmp_province:
        return None
    province_dict = {
        'province_id': tmp_province.province_id,
        'province_code': tmp_province.province_code,
        'province_name': tmp_province.province_name,
        'province_alias': tmp_province.province_alias,
        'province_initial': tmp_province.province_initial,
        'region_id': tmp_province.region_id,
        'regionalism_code': tmp_province.regionalism_code,
        'order_no': tmp_province.order_no,
        'is_show': tmp_province.is_show,
    }

    return province_dict

@redis_func()
def get_city_by_id(city_id=None):
    tmp_city = get_object(model=ModelName.T_BASE_CITY,
                          is_enable=1, is_show=1,
                          city_id=city_id)
    if not tmp_city:
        return None
    city_dict = {
        'city_id': tmp_city.city_id,
        'province_id': tmp_city.province_id,
        'city_code': tmp_city.city_code,
        'city_name': tmp_city.city_name,
        'city_alias': tmp_city.city_alias,
        'is_limited': tmp_city.is_limited,
        'is_capital': tmp_city.is_capital,
        'is_popular': tmp_city.is_popular,
        'is_municipality': tmp_city.is_municipality,
        'regionalism_code': tmp_city.regionalism_code,
        'order_no': tmp_city.order_no,
        'is_show': tmp_city.is_show,
    }

    return city_dict

@redis_func()
def get_county_by_id(county_id=None):
    tmp_county = get_object(model=ModelName.T_BASE_COUNTY,
                            is_enable=1, is_show=1,
                            county_id=county_id)
    if not tmp_county:
        return None
    county_dict = {
        'county_id': tmp_county.county_id,
        'city_id': tmp_county.city_id,
        'county_code': tmp_county.county_code,
        'county_name': tmp_county.county_name,
        'regionalism_code': tmp_county.regionalism_code,
        'order_no': tmp_county.order_no,
        'is_show': tmp_county.is_show,
    }
    return county_dict
