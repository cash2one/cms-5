# -*- coding: utf-8 -*-

import logging
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404
from django.db import connections

from cbbweb.cms import models as cmsmodels
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils import (dictfetchall, str2array)

from cbbweb.service.cms_utils.append_kwargs import append_kwargs

SERVICE_LOGGER = logging.getLogger('service')


@redis_func()
def get_object(model=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    try:
        obj = cmsmodel.objects.get(**kwargs)
    # except ObjectDoesNotExist as exc:
    #     SERVICE_LOGGER.error(str(exc) + "[" + str(kwargs) + "]")
    #     return None
    except ObjectDoesNotExist:
        return None
    return obj


@redis_func()
def list_objs(model=None, offset=None, count=None, orderby=None, exclude=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if exclude:
        objs = objs.exclude(**exclude)
    if orderby:
        orderby = str2array(orderby)
        objs = objs.order_by(*orderby)
    if offset and count:
        offset = int(offset)
        count = int(count)
        objs = objs[offset: offset+count]
    elif offset:
        offset = int(offset)
        objs = objs[offset:]
    elif count:
        count = int(count)
        objs = objs[:count]
    return objs

@redis_func()
def count_objs(model=None, offset=None, count=None, orderby=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if orderby:
        if isinstance(orderby, str):
            orderby = orderby.replace('(', '[')
            orderby = orderby.replace(')', ']')
            orderby = orderby.replace('\'', '"')
            orderby = json.loads(orderby)
        objs = objs.order_by(*orderby)
    if offset and count:
        offset = int(offset)
        count = int(count)
        objs = objs[offset: offset+count]
    elif offset:
        offset = int(offset)
        objs = objs[offset:]
    elif count:
        count = int(count)
        objs = objs[:count]
    return objs.count()

@redis_func()
def get_paginator(model=None, per_page=10, page=1, orderby=None, **kwargs):
    if page is None:
        page = 1
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if orderby:
        orderby = str2array(orderby)
        objs = objs.order_by(*orderby)
    paginator = Paginator(objs, per_page)
    p = paginator.page(page)
    page_dict = {}
    page_dict['paginator'] = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
    }
    page_dict['object_list'] = list(p.object_list.values())

    return page_dict

# ---------------------------------------------
# for rest
# ---------------------------------------------
PRIVATE_TABLE_DICT = {
    'TBaseDealer': [
        'id', 'dlr_code', 'dlr_short_name', 'dlr_full_name', 'dlr_prop',
        'parent_dlr_id', 'dlr_status', 'dlr_level', 'car_series_ids',
        'sale_city_ids', 'group_id', 'email', 'sale_tel', 'service_tel',
        'service_tel_sub', 'insurance_tel', 'urg_sos_tel',
        'mdm_car_brand_code', 'cbb_car_brand_code', 'business_domain',
        'subdivision_business', 'is_vip', 'service_auth',
        'pre_sales_score', 'after_sales_score', 'pre_sales_score_prop',
        'after_sales_score_prop', 'clue_handle_efficiency', 'is_frozen',
        'freeze_reason', 'dlr_image_url',
        'province_id', 'city_id', 'county_id', 'cont_address', 'zip_code',
        'longitude', 'latitude', 'order_no',
        'is_enable'
    ]
}

@redis_func()
def get_object_rest(model=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    try:
        obj = cmsmodel.objects.get(**kwargs)
    # except ObjectDoesNotExist as exc:
    #     SERVICE_LOGGER.error(str(exc) + "[" + str(kwargs) + "]")
    #     return None
    except ObjectDoesNotExist:
        return None
    if model in PRIVATE_TABLE_DICT:
        tmp_obj = {}
        for info in PRIVATE_TABLE_DICT[model]:
            tmp_obj[info] = getattr(obj, info)
        return tmp_obj
    return obj


@redis_func()
def list_objs_rest(model=None, offset=None, count=None, orderby=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if orderby:
        orderby = str2array(orderby)
        objs = objs.order_by(*orderby)
    if offset and count:
        offset = int(offset)
        count = int(count)
        objs = objs[offset: offset+count]
    elif offset:
        offset = int(offset)
        objs = objs[offset:]
    elif count:
        count = int(count)
        objs = objs[:count]
    if model in PRIVATE_TABLE_DICT:
        objs = list(objs.values(*PRIVATE_TABLE_DICT[model]))
    return objs

@redis_func()
def count_objs_rest(model=None, offset=None, count=None, orderby=None, **kwargs):
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if orderby:
        if isinstance(orderby, str):
            orderby = orderby.replace('(', '[')
            orderby = orderby.replace(')', ']')
            orderby = orderby.replace('\'', '"')
            orderby = json.loads(orderby)
        objs = objs.order_by(*orderby)
    if offset and count:
        offset = int(offset)
        count = int(count)
        objs = objs[offset: offset+count]
    elif offset:
        offset = int(offset)
        objs = objs[offset:]
    elif count:
        count = int(count)
        objs = objs[:count]
    return objs.count()

@redis_func()
def get_paginator_rest(model=None, per_page=10, page=1, orderby=None, **kwargs):
    if page is None:
        page = 1
    if not isinstance(model, str):
        model = model.value
    try:
        cmsmodel = getattr(cmsmodels, model)
    except AttributeError:
        raise Http404
    # append is_enable=1 is_show=1 is_frozen=0
    kwargs = append_kwargs(model, kwargs)
    objs = cmsmodel.objects.all()
    if kwargs:
        objs = objs.filter(**kwargs)
    if orderby:
        orderby = str2array(orderby)
        objs = objs.order_by(*orderby)
    paginator = Paginator(objs, per_page)
    p = paginator.page(page)
    page_dict = {}
    page_dict['paginator'] = {
        'count': paginator.count,
        'num_pages': paginator.num_pages,
    }

    if model in PRIVATE_TABLE_DICT:
        page_dict['object_list'] = list(
            p.object_list.values(*PRIVATE_TABLE_DICT[model])
        )
    else:
        page_dict['object_list'] = list(p.object_list.values())

    return page_dict
