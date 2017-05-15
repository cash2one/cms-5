# -*- coding: utf-8 -*-

import logging
import json
from collections import OrderedDict
import requests
import threading
import asyncio
import aiohttp
import datetime


from django.conf import settings
from django.core.cache import (caches, cache)
from django_redis import get_redis_connection
from cbbweb.cms.models import (TBaseCity, TCmsCatalogs, TBaseProvince,
                               TBaseDealer)


logger = logging.getLogger('service')


def cache_site():
    '''
        cache almost site page
    '''
    starttime = datetime.datetime.now()
    # 获取当前缓存位置
    hist_cache_name = cache.get(settings.REDIS_LOCATION, 'default')
    # 获取将要缓存的库
    cache_name = 'second' if hist_cache_name == 'default' else 'default'
    con = get_redis_connection(cache_name)
    # 清空将要缓存的库
    con.flushdb()
    cache.set(settings.REDIS_LOCATION, hist_cache_name)
    # 设置将要缓存的库位置
    cache.set(settings.REDIS_REFRESH_LOCATION, cache_name, 60*60*3)

    print('>>>>>>>>>>cache site data starting<<<<<<<<<<')
    loop = asyncio.get_event_loop()

    catalog_starttime = datetime.datetime.now()
    entrance4catalogs(loop)
    catalog_endtime = datetime.datetime.now()

    dealer_starttime = datetime.datetime.now()
    entrance4dealer(loop)
    dealer_endtime = datetime.datetime.now()

    loop.close()

    endtime = datetime.datetime.now()
    print('>>>>>>>>>>flush catalogs cache cost %s seconds<<<<<<<<<<'
          % (catalog_endtime-catalog_starttime).seconds )
    print('>>>>>>>>>>flush dealers cache cost %s seconds<<<<<<<<<<'
          % (dealer_endtime-dealer_starttime).seconds )
    print('>>>>>>>>>>flush cache cost %s seconds<<<<<<<<<<'
          % (endtime-starttime).seconds )
    # 缓存刷新完毕，切换缓存位置
    cache.set(settings.REDIS_LOCATION, cache_name, None)


def entrance4catalogs(loop):
    citys = TBaseCity.objects.filter(is_enable=1)
    citys = list(citys)
    cross_len = 20

    tasks = [cache_catalogs(citys[i::cross_len]) for i in range(cross_len)]
    loop.run_until_complete(asyncio.wait(tasks))

@asyncio.coroutine
def cache_catalogs(citys):
    catalogs = TCmsCatalogs.objects.filter(is_enable=1)
    for city in citys:
        for catalog in catalogs:
            __url__ = "%s%s%s?__fucku__=1" % (
                settings.APP_DOMAIN, city.city_alias, catalog.cata_full_alias)
            print('>>>>>>>>>>>>>>>>>cacheing catalog %s(%s), url=%s' %
                  (catalog.cata_name, city.city_name, __url__))
            response = yield from aiohttp.request('GET', __url__)
            response.close()
            print('=================finish cache catalog %s(%s)' % (
                catalog.cata_name, city.city_name))

def entrance4dealer(loop):
    catalog = TCmsCatalogs.objects.get(is_enable=1, model_table='t_base_dealer')
    if catalog:
        dealers = TBaseDealer.objects.filter(is_enable=1)
        dealers = list(dealers)
        cross_len = 20

        tasks = [cache_dealers(catalog, dealers[i::cross_len]) for i in range(cross_len)]
        loop.run_until_complete(asyncio.wait(tasks))
    else:
        print("!!!!!!!!!!no dealer catalog to cache!!!!!!!!!!")

@asyncio.coroutine
def cache_dealers(catalog, dealers):
    for dealer in dealers:
        __url__ = "%s%s/%s?__fucku__=1" % (
            settings.APP_DOMAIN, catalog.cata_full_alias, dealer.id)
        print('>>>>>>>>>>>>>>>>>cacheing dealer %s(%s), url=%s' %
                (dealer.dlr_short_name, dealer.dlr_code, __url__))
        response = yield from aiohttp.request('GET', __url__)
        response.close()
        print('=================finish cache dealer %s(%s)' % (
            dealer.dlr_short_name, dealer.dlr_code))
