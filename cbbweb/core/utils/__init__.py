# -*- coding: utf-8 -*-
import json
import logging
import inspect
import traceback
from user_agents import parse
from django.db import connections
from django.db.models.fields.related import ManyToManyField
from django.db.models.query import QuerySet
from django.db import models

from cbbweb.core.utils.db import (connection, dictfetchall, dictfetchone)

logger = logging.getLogger('cms')

from threading import local
app_local_data = local()


def is_mobile(user_agent):
    user_agent = parse(user_agent)
    return user_agent.is_mobile


def get_method_dict(level=1):
    '''
        fetch method's parameter, return dict
    '''
    # get current frame object
    frame = inspect.currentframe()
    # through current frame, get father method frame object
    frame = inspect.getouterframes(frame)[level][0]

    (args, _, _,values) = inspect.getargvalues(frame)
    kw = {}
    for i in args:
        kw[i] = values[i]
    return kw


def str2array(strs):
    if isinstance(strs, str):
        strs = strs.replace('(', '[')
        strs = strs.replace(')', ']')
        strs = strs.replace('\'', '"')
        strs = json.loads(strs)
        return strs
    else:
        return strs


def to_dict(instance):
    '''
    convert model instance fields to dict
    '''
    opts = instance._meta
    data = {}
    for f in opts.concrete_fields + opts.many_to_many:
        if isinstance(f, ManyToManyField):
            if instance.pk is None:
                data[f.name] = []
            else:
                data[f.name] = list(f.value_from_object(
                    instance
                ).values_list('pk', flat=True))
        else:
            data[f.name] = f.value_from_object(instance)
    return data


def convert_obj(obj):
    result = obj
    if isinstance(obj, QuerySet):
        result = list(obj.values())
    elif isinstance(obj, models.Model):
        result = to_dict(obj)
    else:
        pass
    return result


def trace_log(msg=''):
    errorDoc = """
==============================================
message: %s
----------------------------------------------
params : %s
----------------------------------------------
trace  : %s
==============================================
    """ % (msg, get_method_dict(level=2), traceback.format_exc())
    return errorDoc
