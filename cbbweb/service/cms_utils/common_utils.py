# -*- coding: utf-8 -*-


import math
from datetime import datetime

PER_PAGE_MAX = 50

def offset_count(per_page=None, page=None):
    try:
        per_page = int(per_page)
        page = int(page)
        if per_page > PER_PAGE_MAX:
            per_page = PER_PAGE_MAX
        elif per_page == 0:
            per_page = PER_PAGE_MAX
        offset = per_page * (page-1)
        if offset < 0:
            offset = 0
        return (offset, per_page)
    except Exception:
        return (0, 1)

def to_int(val):
    try:
        val = int(val)
    except Exception:
        val = 0
    return val

def to_float(val):
    try:
        val = float(val)
    except Exception:
        val = 0.0
    return val

def to_positive(val):
    try:
        val = int(val)
        if val < 0:
            val = 0
    except Exception:
        val = 0
    return val

def max_int(val):
    try:
        val = int(val)
        if val > PER_PAGE_MAX:
            val = PER_PAGE_MAX
    except Exception:
        val = 0
    return val

def geo_distance(lat1, lng1, lat2, lng2):
    try:
        lat1 = to_float(lat1)
        lng1 = to_float(lng1)
        lat2 = to_float(lat2)
        lng2 = to_float(lng2)
        # earth's mean radius in KM
        r = 6378.137
        lat1 = math.radians(lat1)
        lng1 = math.radians(lng1)
        lat2 = math.radians(lat2)
        lng2 = math.radians(lng2)
        d1 = abs(lat1 - lat2)
        d2 = abs(lng1 - lng2)
        p = (math.pow(math.sin(d1 / 2), 2)
             + math.cos(lat1) * math.cos(lat2) * math.pow(math.sin(d2 / 2), 2))
        dis = r * 2 * math.asin(math.sqrt(p))
        return dis
    except Exception:
        return 0

def int_list_to_str(int_list, join_char=','):
    if not int_list:
        return ''
    try:
        tmp_str = join_char.join(str(tmp_int) for tmp_int in int_list)
        return tmp_str
    except Exception:
        return ''


def get_spend_time(test_func):
    a = datetime.now()
    print('-' * 2 + ' ' 
          + a.strftime('%Y-%m-%d %H:%M:%S') 
          + ' - '
          + test_func.__name__ + '-' * 2)
    test_func()
    b = datetime.now()
    c = (b - a).seconds
    d = (b - a).microseconds
    print(test_func.__name__ + ' : ' + str(c) + 's.' + str(d).rjust(6, '0'))
    print('=' * 2 + ' ' 
          + b.strftime('%Y-%m-%d %H:%M:%S') 
          + ' = '
          + test_func.__name__ + '=' * 2)

def get_spend_time_from_before(before_time, note_str=''):
    print('-' + ' get_spend_time_from_before ' + '-')
    a = before_time
    b = datetime.now()
    c = (b - a).seconds
    d = (b - a).microseconds
    print(note_str + ' : ' + str(c) + 's.' + str(d).rjust(6, '0'))
    print('=' * 20)
    return b

