# -*- coding: utf-8 -*-

import logging
import json
from collections import OrderedDict

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404

from cbbweb.cms import models as cmsmodels
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils import (str2array, to_dict, get_method_dict,
                               convert_obj)
from cbbweb.core.utils import db
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import (list_objs)

logger = logging.getLogger('service')


@redis_func()
def get_city_data():
    '''
        fetch city data, in order to fit the page data
    '''

    sql = """
        SELECT
            province_initial
        FROM
            t_base_province
        WHERE
            province_initial IS NOT NULL and
            is_enable=1 and is_show=1
        GROUP BY province_initial
    """

    province_initials = db.fetch_col_array(sql,{},'province_initial')

    result = OrderedDict()
    if province_initials:
        for letter in province_initials:
            letterArr = result[letter] = []
            provinces = list_objs(model=ModelName.T_BASE_PROVINCE,
                                  province_initial=letter, is_show=1,
                                  is_enable=1, orderby=['regionalism_code'])
            provinces = provinces.values('id', 'province_id',
                                         'province_name', 'province_initial')
            for prov in provinces:
                prov_data = {}
                prov_data['data'] = prov
                _citys = list_objs(model=ModelName.T_BASE_CITY,
                               province_id=prov['id'], is_enable=1, is_show=1,
                               orderby=['regionalism_code'])
                _citys = list(_citys.values('id', 'city_id', 'city_name',
                                            'city_alias'))
                prov_data['citys'] = _citys
                letterArr.append(prov_data)

        return result
    else:
        return None;


@redis_func()
def get_hot_city():
    _citys = list_objs(model=ModelName.T_BASE_CITY, is_popular=1, is_enable=1, is_show=1)
    _citys = list(_citys.values('id', 'city_id', 'city_name', 'city_alias'))
    return _citys


@redis_func()
def get_direct_city():
    _citys = list_objs(model=ModelName.T_BASE_CITY, is_municipality=1, is_enable=1, is_show=1)
    _citys = list(_citys.values('id', 'city_id', 'city_name', 'city_alias'))
    return _citys
