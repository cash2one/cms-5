# -*- coding: utf-8 -*-

import textwrap

from datetime import datetime

import json
import jinja2

from urllib import parse

from jinja2 import Template

from django_jinja import library
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder

from cbbweb import service
from cbbweb.core.utils import convert_obj
from cbbweb.core.utils.http import CbbJSONEncoder
from cbbweb.service.catalogs_service import get_catalog_url

from django.conf import settings
from django.shortcuts import render


@library.filter
def kidding(name):
    """
    Usage: {{ 'Hello'|mylower() }}
    """
    return name.lower()


@library.global_function
@jinja2.contextfunction
def city_url(context, *args, **kwargs):
    view_name = args[0]
    citycode = context['request'].GET.get('citycode')
    if kwargs:
        kwargs['citycode'] = citycode
        args = ()
    else:
        args = [citycode] + list(args[1:])

    return reverse(view_name, args=args, kwargs=kwargs)


@library.global_function
@jinja2.contextfunction
def catalog_url(context, path=None, model_table=None,
                model_instanceid=None):
    citycode = context['request'].GET.get('citycode')
    kwargs = {}
    kwargs['citycode'] = citycode
    args = ()

    if path:
        kwargs['catalog_url'] = path.lstrip('/')
        return reverse('parse_alias', args=args, kwargs=kwargs)

    if model_table and model_instanceid:
        _url = get_catalog_url(model_table=model_table,
                               model_instanceid=model_instanceid)
        kwargs['catalog_url'] = _url.lstrip('/')
        return reverse('parse_alias', args=args, kwargs=kwargs)

    if model_table:
        _url = get_catalog_url(model_table=model_table)
        kwargs['catalog_url'] = _url.lstrip('/')
        return reverse('parse_alias', args=args, kwargs=kwargs)

    return 'no path found'


# base model tags
@library.global_function
def get_object(tablename, **kwargs):
    kwargs['model'] = tablename
    return service.get_object(**kwargs)


@library.global_function
def list_objs(**kwargs):
    return service.list_objs(**kwargs)


@library.global_function
def count_objs(**kwargs):
    return service.count_objs(**kwargs)


@library.global_function
def page_objs(**kwargs):
    return service.get_paginator(**kwargs)


# service api tags
@library.global_function
def run(service_name, **kwargs):
    '''
    service_name is a enum of class ServiceName(Enum)
    '''
    try:
        (lib_path, method_name) = service_name.value
        module_home = __import__(lib_path, globals(), locals(), [method_name])
        service_func = getattr(module_home, method_name)
    except AttributeError:
        raise Http404

    if not settings.CHX_DEBUG:
        result = service_func(**kwargs)
    else:
        print('-' * 10 + ' run ' + service_name.name + ' ' + '-' * 10)
        a = datetime.now()
        result = service_func(**kwargs)
        b = datetime.now()
        c = (b - a).seconds
        d = (b - a).microseconds
        print(service_name.name + ' : ' + str(c) + 's.' + str(d).rjust(6, '0'))
        print('=' * 20)
    
    return result

@library.global_function
@jinja2.contextfunction
def rest(context, rest_name, **kwargs):
    citycode = context['request'].GET.get('citycode')
    if 'model' in kwargs:
        kwargs['model'] = kwargs['model'].value
    service_name = rest_name.name.lower()
    if kwargs:
        urlparam = parse.urlencode(kwargs)
        url = (reverse(u'cbbweb.rest',
                       kwargs={"citycode": citycode,
                               "service_name": service_name})
               + '?' + urlparam)
    else:
        url = reverse(u'cbbweb.rest',
                      kwargs={"citycode": citycode,
                              "service_name": service_name})
    return url


@library.global_function
def dumps_json(obj, add_pre=False):
    json_str = json.dumps(convert_obj(obj),
                          ensure_ascii=False,
                          indent=4,
                          cls=CbbJSONEncoder)
    if add_pre:
        json_str = '<pre>' + json_str + '</pre>'
    return json_str


@library.global_function
@jinja2.contextfunction
def get_city(context):
    return context['request'].POST.get('city')

@library.global_function
def datetime_now():
    return datetime.now()

@library.global_function
def api_doc(api_service):
    (lib_path, method_name) = api_service
    module_home = __import__(lib_path, globals(), locals(), [method_name])
    service_func = getattr(module_home, method_name)
    doc_str = service_func.__doc__
    format_str = ''

    if doc_str:
        try:
            # pip install docutils
            from docutils.core import publish_parts
            doc_str = textwrap.dedent(doc_str)
            extra_settings = {
                'initial_header_level': 4,
                'doctitle_xform': 0,
                'syntax_highlight': 'short'
            }
            document = publish_parts(doc_str,
                                     writer_name='html',
                                     settings_overrides=extra_settings)
            format_str = document['body']
        except ImportError:
            format_str = doc_str
    
    return format_str

@library.global_function
@jinja2.contextfunction
def save_page(context, template_path, save_path):
    if not settings.DEBUG:
        return False
    base_path = settings.BASE_DIR
    src_template_path = settings.TEMPLATES[1]['DIRS'][0]
    save_path = base_path + '/' + src_template_path + '/' + save_path
    save_file = open(save_path, 'w')
    if save_file:
        r = render(None, template_path, context)
        save_file.write(str(r.content, encoding="utf-8"))
        save_file.close()
    return True
    
@library.global_function
def dir_obj(obj):
    if not settings.DEBUG:
        return None
    return dir(obj)
