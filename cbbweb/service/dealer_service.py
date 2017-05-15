# -*- coding: utf-8 -*-

import logging

from cbbweb.core.utils import str2array
from cbbweb.core.utils import get_method_dict
from cbbweb.core.utils import db
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName

from cbbweb.service import list_objs

logger = logging.getLogger('service')
PER_PAGE_MAX = 50

@redis_func()
def get_car_series_newest_activity(city_id=None,car_series_id_list=[]):
    '''
        以车系为维度，查询最新的活动
        返回值:
            活动列表
    '''
    if not city_id:
        logger.warn("no city choose, means whole country?")
    if not car_series_id_list:
        logger.warn("car_series_id_list can not be empty.")
        return None

    kw = get_method_dict()
    kw['car_series_id_list'] = str2array(car_series_id_list)

    sql = """
        select
        max(id) id
        from t_base_media_activity
        where
        car_series_id is not null
        and car_series_id in %(car_series_id_list)s
        {% if city_id -%}
        and city_id = %(city_id)s
        {%- endif %}
        group by car_series_id
    """
    ids = db.fetch_col_array(sql, kw, 'id')

    activitys = list_objs(model=ModelName.T_BASE_MEDIA_ACTIVITY, id__in=ids)
    return activitys


@redis_func()
def get_car_series_newest_activity_dict(*args, **kwargs):
    '''
        以车系为维度，查询最新的活动
        返回值：
            以车系ID为KEY,活动为VALUE
    '''
    activitys = get_car_series_newest_activity(*args, **kwargs)
    kw = {}
    for activity in activitys.values():
        kw[activity['car_series_id']] = activity
    return kw

