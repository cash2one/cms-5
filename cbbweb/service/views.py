# -*- coding: utf-8 -*-

import json
import logging
from django.http import HttpResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder

from cbbweb.core.utils.constants import API
from cbbweb.core.utils import (convert_obj, trace_log)
from cbbweb.core.utils.http import (CbbJsonResponse, get_ip)

# from cbbweb.service.page.home import home_api

# print('======== test begin')
# home_api.traverse_all()
# print('======== test end')


logger = logging.getLogger('service')

STATUS_ERROR = "error"
STATUS_SUCCESS = "success"

PRIVATE_SERVICE_LIST = [
    'get_object',
    'list_objs',
    'count_objs',
    'get_paginator'
]
INJECT_IP_SERVICE_LIST = [
    ('cbbweb.service.sms_service', 'send_verify_code'),
]
PRIVATE_SERVICE_POSTFIX = '_rest'

def rest(request, citycode='beijing', service_name=None):
    extra_data = {}
    try:
        service_api = getattr(API, service_name.upper())
        (lib_path, method_name) = service_api.value
        if method_name in PRIVATE_SERVICE_LIST:
            method_name += PRIVATE_SERVICE_POSTFIX
        if (lib_path, method_name) in INJECT_IP_SERVICE_LIST:
            extra_data['ip'] = get_ip(request)
        module_home = __import__(lib_path, globals(), locals(), [method_name])
        service_func = getattr(module_home, method_name)
    except AttributeError as e:
        logger.error(e)
        raise Http404
    if request.method == 'GET':
        req = request.GET.copy()
        return handle_request(request, service_func, req, extra_data)
    elif request.method == 'POST':
        req = request.POST.copy()
        return handle_request(request, service_func, req, extra_data)
    raise Http404

def handle_request(request, service_func, data, extra_data):
    result = {
        "status": STATUS_ERROR,
    }
    if 'citycode' in data:
        del data['citycode']
    if 'csrfmiddlewaretoken' in data:
        del data['csrfmiddlewaretoken']
    kwargs = {}
    for k, v in data.items():
        kwargs[k] = v
    kwargs.update(extra_data)
    try:
        val = service_func(**kwargs)
    except Exception as e:
        logger.error(trace_log())
        raise Http404
    val = convert_obj(val)
    result['result'] = val
    result['status'] = STATUS_SUCCESS
    return CbbJsonResponse(result)
