# -*- coding: utf-8 -*-
import logging
from django.db import connections
from jinja2 import Template

logger = logging.getLogger('cms')


def connection():
    return connections['cms']

def connection_core():
    return connections['default']

def dictfetchall(cursor):
    """Returns all rows from a cursor as a dict"""
    desc = cursor.description
    return [
        dict(zip([col[0] for col in desc], row))
        for row in cursor.fetchall()
    ]


def dictfetchone(cursor):
    """Returns all rows from a cursor as a dict"""
    data = cursor.fetchone()
    if not data:
        return None
    desc = cursor.description
    return dict(zip([col[0] for col in desc], data))


def fetch(sql, param={}):
    cursor = connection().cursor()
    sql = Template(sql).render(param)
    cursor.execute(sql, param)
    objs = dictfetchall(cursor)
    return objs


def fetchone(sql, param={}):
    cursor = connection().cursor()
    sql = Template(sql).render(param)
    cursor.execute(sql, param)
    obj = dictfetchone(cursor)
    return obj


def fetch_col_array(sql, param={}, key={}):
    objs = fetch(sql,param)
    return [obj[key] for obj in objs ]


