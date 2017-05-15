#!/usr/bin/env python
# coding: utf-8

import requests
import re
import json, os, sys, logging, threading, time,imp
from simplemysql import SimpleMysql
from configparser import RawConfigParser
import configparser
INI_PATH = 'sync.cfg'
DEBUG = True
LOG_LEVEL = logging.INFO

class myconf(configparser.RawConfigParser):
    def __init__(self,defaults=None):
        configparser.RawConfigParser.__init__(self,defaults=None)
    def optionxform(self, optionstr):
        return optionstr


class Ini():
    def __init__(self):
        self.config = myconf()


    def get_items(self, section='MySQL'):
        self.config.read(INI_PATH)
        return dict(self.config.items(section))


    def get_value(self, section, option):
        self.config.read(INI_PATH)
        return self.config.get(section, option)

    def set_updatedate(self, function,time):
        self.config.read(INI_PATH)
        self.config.set(function, 'updatedDate', time)
        self.config.write(open(INI_PATH, "w"))


    def get_all_biz(self):
        self.config.read(INI_PATH)
        sections = self.config.sections()

        ini = Ini()
        result = {}
        for section in sections:
            if section not in ('MySQL', 'API'):
                result[section] = ini.get_items(section)

        return result,sections

class GetData():
    url = ''

    def __init__(self, url=None):
        if url:
            self.url = url
        else:
            ini = Ini()
            urls = dict(ini.get_items(section='API'))
#       False就选择Info，True就选择info
            self.url = DEBUG and urls['debug'] or urls['production']


    def from_e4s(self, function, kwargs):
        api_url = self.url % (function)
        logging.info(api_url)
        return requests.post(url=api_url, data=kwargs).text

class SetData():
    def __init__(self):
        dbc = ini.get_items('MySQL')
        self.db = SimpleMysql(host=dbc['host'], db=dbc['db'], user=dbc['user'], passwd=dbc['passwd'])

    def to_mysql(self, function, kwargs, time,table):
        if not table: return

        l,id = self.db.IsExistsinSQL(table, dict(kwargs))
        if l == 0:
            result = self.db.insert(table, dict(kwargs))
        elif l == 1:
            result = self.db.update(table, dict(kwargs),id)
        self.db.commit()
        logging.info('Complete sync - function: %s, table: %s, result: %s' % (function, table, result))


def Process(function,kwargs):
    channel = 'mysql'
    logging.info('Starting to sync - channel: %s, function: %s, args: %s' % (channel, function, kwargs))
#取出对应function，data
    gd = GetData()
    data = gd.from_e4s(function,kwargs)
    data = json.loads(data)
    if int(data['retnCode']) != 0:
        logging.error(str(data))
    if data['results']!=None:
        updatetime = data['retnDate']
        table = data['retnTable']
        data = data['results']
        sd = SetData()
        if channel == 'tmall':
            return sd.to_api(function, data)

        for i in range(len(data)):
            dictdata=data[i]
            sd.to_mysql(function, dictdata,updatetime,table)

        ini = Ini()
        # 完成保存时间
        ini.set_updatedate(function,updatetime)


if __name__ == '__main__':
    imp.reload(sys)
#    sys.setdefaultencoding('utf-8')
    logging.basicConfig(level=LOG_LEVEL, format='[%(asctime)s] %(levelname)s: %(message)s', filename='sync.py.log', filemode='a')
    console = logging.StreamHandler()
    console.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s'))
    logging.getLogger('').addHandler(console)
    try:
        ini = Ini()
        apis,sections2 = ini.get_all_biz()
        for api in apis:
            if apis[api].pop('enable') == 'True':
                # cartypepropertytemplate cartypeproperty offerprice
                Process(api, apis[api])
                time.sleep(1)

    except Exception as e:
       logging.error(e)

