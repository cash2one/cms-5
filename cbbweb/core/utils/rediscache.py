# -*- coding: utf-8 -*-

import re
import logging
from functools import wraps

from django.core.cache import (caches, cache)
from django.conf import settings

from cbbweb.core.utils import (app_local_data)


CACHE_NONE = '[-:None:-]'

KEY_SEPARATOR = ':'
KEY_REPLACE = '_'

REPLACE_RE = re.compile(r"[ \'\"]")
logger = logging.getLogger('service')

def redis_func(timeout=60*60*25, prefix=''):
    '''
    Passing in None for timeout will cache the value forever.
    A timeout of 0 won’t cache the value.
    '''
    def _deco(func):
        @wraps(func)
        def __deco(*args, **kwargs):
            overload = False
            try:
                logger.info("============Focus to update cache ? result is %s",
                            app_local_data.force_to_update_cache)
                overload = app_local_data.force_to_update_cache
            except AttributeError as e:
                pass
            # if(settings.DEBUG):
            #     return func(*args, **kwargs)
            if not settings.CACHEING:
                return func(*args, **kwargs)

            cur_cache = get_cache()

            key = (
                prefix + KEY_SEPARATOR
                + func.__name__ + KEY_SEPARATOR
                + str(args) + KEY_SEPARATOR
                + str(kwargs)
            )
            # replace special char ' " to _
            key = REPLACE_RE.sub(KEY_REPLACE, key)
            # obj = cache.get(key)
            obj = cur_cache.get(key, CACHE_NONE)
            # if not obj or overload:
            if (obj == CACHE_NONE) or overload:
                obj = func(*args, **kwargs)
                cur_cache.set(key, obj, timeout)
                return obj
                # obj = func(*args, **kwargs)
                # if obj:
                #     cur_cache.set(key, obj, timeout)
                #     return obj
                # else:
                #     return obj
            else:
                return obj
        return __deco
    return _deco

def get_cache():
    cache_name = cache.get(settings.REDIS_LOCATION, 'default')
    cur_cache = caches[cache_name]
    try:
        logger.info("============Refresh cache to you ? result is %s",
                    app_local_data.refresh_cache_to_you)
        if app_local_data.refresh_cache_to_you:
            refresh_cache_name = cache.get(settings.REDIS_REFRESH_LOCATION)
            if refresh_cache_name:
                cur_cache = caches[refresh_cache_name]
    except AttributeError as e:
        pass

    return cur_cache


def set_func_cache(func, val, *args, **kwargs):
    prefix = ''
    key = (
        prefix + KEY_SEPARATOR
        + func.__name__ + KEY_SEPARATOR
        + str(args) + KEY_SEPARATOR
        + str(kwargs)
    )
    # replace special char ' " to _
    key = REPLACE_RE.sub(KEY_REPLACE, key)
    cache.set(key, val)

def get_func_cache(func, *args, **kwargs):
    prefix = ''
    key = (
        prefix + KEY_SEPARATOR
        + func.__name__ + KEY_SEPARATOR
        + str(args) + KEY_SEPARATOR
        + str(kwargs)
    )
    # replace special char ' " to _
    key = REPLACE_RE.sub(KEY_REPLACE, key)
    obj = cache.get(key)
    return obj
