# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from datetime import datetime


class CbbJSONEncoder(DjangoJSONEncoder):

    def default(self, obj):
        if isinstance(obj, datetime):
            serial = obj.strftime('%Y-%m-%d %H:%M:%S')
            return serial
        return super(CbbJSONEncoder, self).default(obj)


class CbbJsonResponse(HttpResponse):
    def __init__(self, data, encoder=CbbJSONEncoder, safe=True,
                 json_dumps_params=None, **kwargs):
        if json_dumps_params is None:
            json_dumps_params = {}
        kwargs.setdefault('content_type', 'application/json')
        data = json.dumps(data, cls=encoder, **json_dumps_params)
        super(CbbJsonResponse, self).__init__(content=data, **kwargs)


def get_ip(request):
    ip = None
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
    else:
        ip = request.META['REMOTE_ADDR']
    return ip
