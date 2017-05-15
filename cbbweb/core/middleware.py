# -*- coding: utf-8 -*-
import requests
import pypinyin
import logging
import os
from django.conf import settings
from cbbweb.core.utils.ipip import (IP, IPX)
from django.http import HttpResponseRedirect
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import (get_object, list_objs)
from cbbweb.core.utils import (to_dict, app_local_data, trace_log)
from cbbweb.core.utils.http import (get_ip)


logger = logging.getLogger('cms')
LOC_API = \
    'http://api.map.baidu.com/location/ip?ak=zZNfchNgNyP7CkXWDSqA5Hul&ip=%s'
IPX.load(os.path.abspath(settings.BASE_DIR+"/ip.datx"))


class CbbMiddleware(object):

    def __init__(self):
        pass

    def process_response(self, request, response):
        '''
            http://zhanzhang.baidu.com/college/documentinfo?id=481&page=5
            【Vary HTTP 标头】
            其作用在百度的文档里解释得很清楚：
            1、它会向百度传递一个信号，表示说这是个代码适配的站点， 百度就会尽快
            把网站抓取一遍进行适配；
            2、它可以防止用户接收到错误的网页缓存。这部分是在网站的服务器上进行
            的，有可能是 Nginx,Apache, IIS 等，需要在服务器的配置里，设置
            Varyheader 为 Vary:Accept-Encoding, User-Agent

            【Meta applicable-device 标签】
            在pc模板head中添加
        　　<meta name="applicable-device" content="pc">
        　　在移动模板head中添加
        　　<meta name="applicable-device" content="mobile">
        '''
        response['Vary'] = 'Accept-Encoding, User-Agent'
        return response

    def process_request(self, request):
        '''
            1. check path, using '/' to split
            2. if the first path is a citycode, return
            3. if not, load the citycode by baidu-api, redirect
        '''

        # get the force to update cache param
        if request.GET.get('__ftuc', False):
            app_local_data.force_to_update_cache = True
            request.GET._mutable = True
            request.GET.__delitem__('__ftuc')
            request.GET._mutable = False

        # refresh cache to you, work for cache refresh kit
        if request.GET.get('__fucku__', False):
            app_local_data.refresh_cache_to_you = True
            request.GET._mutable = True
            request.GET.__delitem__('__fucku__')
            request.GET._mutable = False

        path_splits = request.path.split('/')

        citys = []
        if '' != path_splits[1]:
            citys = list_objs(model=ModelName.T_BASE_CITY, count=1,
                             city_alias=path_splits[1])
        city = citys[0] if len(citys) == 1 else None
        if not city:
            #city = self._loadcity(request)
            city = self._local_localcity(request)
        else:
            city = to_dict(city)
            city['confirm'] = True

        request.GET._mutable = True
        request.GET.__setitem__('citycode', city['city_alias'])
        request.GET._mutable = False

        # save the city data to local thread
        app_local_data.city = city

        if path_splits[1] == '__debug__':
            return

        if path_splits[1] == city['city_alias']:
            return
        else:
            return HttpResponseRedirect('/%s%s' % (city['city_alias'],
                                                   request.get_full_path()))


    def _local_localcity(self, request):

        _default_regionalism_code = '110000' #北京
        _city = None
        try:
            addrs = self._locatedcity(request)
            _prov_name,  _city_name, _regionalism_code = addrs[1], addrs[2], addrs[9]

            # lan address
            if _prov_name in (u'本机地址', u'局域网', ''):
                logger.warn('this is a lan address, can not located,'
                            'default to beijing')
                _citys= list_objs(model=ModelName.T_BASE_CITY, count=1, is_enable=1,
                                regionalism_code=_default_regionalism_code)
                _city = to_dict(_citys[0])
                _city['confirm'] = False
                return _city

            # located city fail, jump to provincial capital
            if _city_name == '':
                _province = get_object(model=ModelName.T_BASE_PROVINCE, is_enable=1,
                                regionalism_code=_regionalism_code)
                _city = get_object(model=ModelName.T_BASE_CITY, is_enable=1,
                                province_id=_province.province_id, is_capital=1)
                logger.warn('city can not located, now auto jump to '
                            'provincial capital(%s)', _city.city_name)
                _city = to_dict(_city)
                _city['confirm'] = False
                return _city

            # located city successful
            _city = get_object(model=ModelName.T_BASE_CITY,
                            regionalism_code=_regionalism_code)
            if not _city:
                _city = get_object(model=ModelName.T_BASE_CITY,
                            regionalism_code=_default_regionalism_code)

            _city = to_dict(_city)
            _city['confirm'] = True
            return _city
        except:
            _city = get_object(model=ModelName.T_BASE_CITY,
                            regionalism_code=_regionalism_code)
            _city = to_dict(_city)
            _city['confirm'] = False
            return _city



    def _locatedcity(self, request):
        '''
            ==========================
            use ipip.net interface
            ==========================
            the return data :
            [
                "中国",                // 国家
                "天津",                // 省会或直辖市（国内）
                "天津",                // 地区或城市 （国内）
                "",                   // 学校或单位 （国内）
                "鹏博士",              // 运营商字段（只有购买了带有运营商版本的数据库才会有）
                "39.128399",          // 纬度     （每日版本提供）
                "117.185112",         // 经度     （每日版本提供）
                "Asia/Shanghai",      // 时区一, 可能不存在  （每日版本提供）
                "UTC+8",              // 时区二, 可能不存在  （每日版本提供）
                "120000",             // 中国行政区划代码    （每日版本提供）
                "86",                 // 国际电话代码        （每日版本提供）
                "CN",                 // 国家二位代码        （每日版本提供）
                "AP"                  // 世界大洲代码        （每日版本提供）
            ]
        '''
        ip = get_ip(request)

        try:
            addrs = IPX.find(ip)
            # 116.21.165.216 218.107.1.124
            # addrs = IP.find(ip)

            addrs = addrs.split("\t")
            logger.info("==========pipi ip located===========")
            logger.info(addrs)
            logger.info("====================================")
            return addrs
        except Exception as err:
            logger.error(trace_log('pipi located error'))
            return ['']*14


    def _loadcity(self, request):
        '''
            load city by baidu api
            api doc: http://developer.baidu.com/map/index.php?title=webapi/ip-api
            api result example:
                {
                    address: "CN|北京|北京|None|CHINANET|1|None",   #地址
                    content:       #详细内容
                    {
                        address: "北京市",   #简要地址
                        address_detail:      #详细地址信息
                        {
                            city: "北京市",        #城市
                            city_code: 131,       #百度城市代码
                            district: "",           #区县
                            province: "北京市",   #省份
                            street: "",            #街道
                            street_number: ""    #门址
                        },
                        point:               #百度经纬度坐标值
                        {
                            x: "116.39564504",
                            y: "39.92998578"
                        }
                    },
                    status: 0     #返回状态码
                }
        '''
        _citycode = 'beijing'
        _city = None

        if 'HTTP_X_FORWARDED_FOR' in request.META:
            ip = request.META['HTTP_X_FORWARDED_FOR'].split(',')[-1].strip()
        else:
            ip = request.META['REMOTE_ADDR']

        logger.info(request.META)

        logger.info("user ip is %s" % (ip))

        res = requests.get(LOC_API % ip)
        # if object isn't json, will throw ValueError: No JSON object could be decoded
        # TODO handle json exception
        res_content = res.json()
        if(res_content is not None and res_content['status'] != 0):
            logger.warn("baidu api located fail, status:%s" % (ip))
            logger.warn("located default to beijing.")
            _citys= list_objs(model=ModelName.T_BASE_CITY, count=1,
                             city_alias=_citycode)
            _city = to_dict(_citys[0])
            _city['confirm'] = False
            return _city

        logger.info("=======Baidu Api Result=========")
        logger.info(res.json())
        logger.info("================================")
        addrSplit = res_content['address'].split('|')
        _city_name = addrSplit[2]
        _city = None
        if _city_name == 'None' and addrSplit[1]:
            logger.warn("baidu api can not located city, just located "
                        "in province %s", addrSplit[1])
            logger.warn("default to located to Capital")
            _province = get_object(model=ModelName.T_BASE_PROVINCE,
                       province_name=addrSplit[1])
            _city = get_object(model=ModelName.T_BASE_CITY,
                               province_id=_province.id, is_capital=1)
            _city_name = _city.city_name
            _city = to_dict(_city)
            _city['confirm'] = False
        else:
            _city = get_object(model=ModelName.T_BASE_CITY, city_name=_city_name)
            _city = to_dict(_city)
            _city['confirm'] = True


        logger.info("baidu api located result city:%s" % (_city_name))
        return _city
