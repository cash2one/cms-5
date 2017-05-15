# -*- coding: utf-8 -*-


from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName

from cbbweb.service import get_object
from cbbweb.service import list_objs
from cbbweb.service.catalogs_service import URL
from cbbweb.service.catalogs_service import get_cms_sub_url
from cbbweb.service.cms_utils import common_utils
from cbbweb.service.cms_utils import car_series_utils

MAX_ACTIVITY_COUNT = 10



@redis_func()
def activity_url(activity_type, created_date, activity_id):
    url = get_cms_sub_url(
        URL.ACTIVITY_DEALER,
        str(activity_type)
        + '/'
        + str(created_date)[:7].replace('-', '')
        + '/'
        + str(activity_id)
    )
    return url

@redis_func()
def activity_type_name(activity_type):
    media_activity_type = get_object(model=ModelName.T_BASE_MEDIA_ACTIVITY_TYPE,
                                     is_enable=1,
                                     activity_type=activity_type)
    if not media_activity_type:
        return ""
    return media_activity_type.remark

@redis_func()
def get_activity_by_id(activity_id=None):
    """
        根据活动ID返回活动实例
    """
    activity_id = common_utils.to_int(activity_id)
    tmp_activity = get_object(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                              is_enable=1,
                              id=activity_id)
    if not tmp_activity:
        return None
    activity_dict = {
        'id': tmp_activity.id,
        'url': activity_url(tmp_activity.activity_type,
                            tmp_activity.created_date,
                            tmp_activity.id),
        'activity_title': tmp_activity.activity_title,
        'page_url': tmp_activity.page_url,
        'activity_content': tmp_activity.activity_content,
        'activity_begin_date': tmp_activity.activity_begin_date,
        'activity_end_date': tmp_activity.activity_end_date,
        'activity_type': tmp_activity.activity_type,
        'activity_type_name': activity_type_name(tmp_activity.activity_type),
        'dealer_id': tmp_activity.dealer_id,
        'car_type_id': tmp_activity.car_type_id,
        'car_series_id': tmp_activity.car_series_id,
        'car_brand_id': tmp_activity.car_brand_id,
        'city_id': tmp_activity.city_id,
        'county_id': tmp_activity.county_id,
        'created_date': tmp_activity.created_date,
        'updated_date': tmp_activity.updated_date,
    }

    activity_dict['series'] = {}
    if tmp_activity.car_series_id:
        tmp_car_series = car_series_utils.get_carseries_by_id(
            car_series_id=tmp_activity.car_series_id
        )
        if tmp_car_series:
            activity_dict['series'] = tmp_car_series

    return activity_dict

@redis_func()
def get_activity_list_by_dealer(dealer_id=None, activity_type=2):
    dealer_id = common_utils.to_int(dealer_id)
    activity_type = common_utils.to_int(activity_type)
    activity_ids = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                             is_enable=1,
                             orderby=['-created_date'],
                             count=MAX_ACTIVITY_COUNT,
                             activity_type=activity_type,
                             dealer_id=dealer_id)
    activity_ids = activity_ids.values_list('id', flat=True)
    activity_list = []
    for activity_id in activity_ids:
        tmp_activity = get_activity_by_id(activity_id=activity_id)
        activity_list.append(tmp_activity)
    return activity_list

@redis_func()
def get_activity_list_by_dealer_series(dealer_id=None, car_series_id=None):
    dealer_id = common_utils.to_int(dealer_id)
    car_series_id = common_utils.to_int(car_series_id)
    activity_ids = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                             is_enable=1,
                             orderby=['-created_date'],
                             count=MAX_ACTIVITY_COUNT,
                             activity_type=1,
                             dealer_id=dealer_id,
                             car_series_id=car_series_id)
    activity_ids = activity_ids.values_list('id', flat=True)
    activity_list = []
    for activity_id in activity_ids:
        tmp_activity = get_activity_by_id(activity_id=activity_id)
        activity_list.append(tmp_activity)
    return activity_list

@redis_func()
def get_activity_list_by_city_series(city_id=None, car_series_id=None):
    city_id = common_utils.to_int(city_id)
    car_series_id = common_utils.to_int(car_series_id)
    activity_ids = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY,
                             is_enable=1,
                             orderby=['-created_date'],
                             count=MAX_ACTIVITY_COUNT,
                             activity_type=1,
                             city_id=city_id,
                             car_series_id=car_series_id)
    activity_ids = activity_ids.values_list('id', flat=True)
    activity_list = []
    for activity_id in activity_ids:
        tmp_activity = get_activity_by_id(activity_id=activity_id)
        activity_list.append(tmp_activity)
    return activity_list
