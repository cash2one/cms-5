# -*- coding: utf-8 -*-

import logging

from enum import Enum
from django.db.models import Q

from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils import (str2array, to_dict, get_method_dict)
from cbbweb.core.utils import db
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import (get_object, list_objs)

from cbbweb.core.utils import (app_local_data, trace_log)

logger = logging.getLogger('service')


@redis_func()
def get_catalog_url(model_table=None, model_instanceid=0):
    '''
        根据表名与主键，查询对应的频道URL
    '''
    kw = get_method_dict()
    if kw:
        kw['is_enable'] = 1
    catalog = get_object(model=ModelName.T_CMS_CATALOGS, **kw)
    if not catalog:
        return None
    return catalog.cata_full_alias

@redis_func()
def get_sub_catalog_url(model_table=None, model_instanceid=None, sub_key=None):
    '''
        根据表名与主键，查询对应的频道URL
    '''
    kw = get_method_dict()
    if kw:
        kw['is_enable'] = 1
    if 'sub_key' in kw:
        del kw['sub_key']
    catalog = get_object(model=ModelName.T_CMS_CATALOGS, **kw)
    if not catalog:
        return None
    return catalog.cata_full_alias + '/' + str(sub_key) + '/'


class URL(Enum):
    # 惠挑车
    CAR = "/car"
    # 找好店
    DEALER = "/dealer"
    # 享活动
    ACTIVITY = "/activity"
    # 经销商活动
    ACTIVITY_DEALER = "/activity/dealer"
    # 任性贷
    FINANCE = "/finance"
    # 关于我们
    ABOUT = "/about"
    # 金融列表
    FINANCELIST = "/financelist"
    # 公共留资
    LEAVEMESS = "/leavemess"

@redis_func()
def add_city_alias_url(url):
    """
        在参数url的前面添加城市别名
    """
    return url
    # city_alias = app_local_data.city['city_alias']
    # return '/' + city_alias + url

@redis_func()
def get_cms_url(url):
    """
        返回class URL对应的url
    """
    return add_city_alias_url(url.value)

@redis_func()
def get_cms_sub_url(url, sub_key):
    """
        为参数url添加上子url
    """
    return add_city_alias_url(url.value + '/' + str(sub_key) + '/')

@redis_func()
def get_car_series_url(car_series_id):
    '''
        根据车系ID获取对应的车系的URL
    '''
    catalog = get_object(model=ModelName.T_CMS_CATALOGS,
                         is_enable=1, as_search_result=1,
                         model_table=ModelName.T_BASE_CAR_SERIES.name,
                         model_instanceid=car_series_id)
    if not catalog:
        return None
    result_url = catalog.cata_full_alias
    return add_city_alias_url(result_url)

@redis_func()
def get_car_type_url(car_series_id, car_type_id):
    '''
        根据车系ID和车型ID获取对应的车型的URL
    '''
    catalog = get_object(model=ModelName.T_CMS_CATALOGS,
                         is_enable=1, as_search_result=1,
                         model_table=ModelName.T_BASE_CAR_SERIES.name,
                         model_instanceid=car_series_id)
    if not catalog:
        return None
    result_url = catalog.cata_full_alias + '/' + str(car_type_id) + '/'
    return add_city_alias_url(result_url)

@redis_func()
def get_search_result(words=None, *args, **kwargs):
    catalogs = list_objs(model=ModelName.T_CMS_CATALOGS, as_search_result=1)
    if words:
        catalogs = catalogs.filter((Q(cata_name__contains=words)
                                    | Q(cata_alias__contains=words)))
    catalogs = list(catalogs.values('id', 'cata_name', 'cata_full_alias'))
    logger.info(catalogs)
    return catalogs
