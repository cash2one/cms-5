# -*- coding: utf-8 -*-

import json
import datetime
import requests

from django.conf import settings
from cbbweb.cms import models as cmsmodels
from cbbweb.core.models import TSyncConfig
from cbbweb.core.models import TSyncRecode


def get_data(updateddate, name_api):
    url_api = settings.SQL_URL % name_api
    data = requests.post(url=url_api, data=updateddate).text
    data = json.loads(data)
    return data, url_api

def insert_recode(data, name_api, url_api, updateddate):
    last_use_time = datetime.datetime.now()
    len_data = len(data['results'])
    host = url_api[:37]
    url_left = url_api[37:]
    recode_dict = {}
    recode_dict['name'] = name_api
    recode_dict['create_time'] = last_use_time
    recode_dict['len_data'] = len_data
    recode_dict['host'] = host
    recode_dict['url'] = url_left
    recode_dict['sync_type'] = '0'
    recode_dict['params'] = updateddate
    q = TSyncRecode(**recode_dict)
    q.save()
    return q


def get_configInfo(object_config):
    name_api = object_config.name
    enable = object_config.is_enable
    date = str(object_config.updated_date)[:19]
    updateddate = {}
    updateddate['updatedDate'] = date
    if enable == 1:
        data, url_api = get_data(updateddate, name_api)    
        q = insert_recode(data, name_api, url_api, updateddate)
        if int(data['retnCode']) != 0:
            print('retnCode Wrong!')
        if data['results'] != None:
            updatetime = data['retnDate']
            deltatime = datetime.datetime.strptime(updatetime, '%Y-%m-%d %H:%M:%S')
            table = data['retnTable']
            q.table_name = table
            q.save()
            data = data['results']
            tablename = table.replace('_', ' ').title().replace(' ', '')

            for i in range(len(data)):
                cms_dict = {}
                for key in data[i]:
                    lower_key = key.lower()
                    cms_dict[lower_key] = data[i][key]
                cmsmodel = getattr(cmsmodels, tablename)
                obj = cmsmodel(**cms_dict)
                obj.save()

            object_config.updated_date = deltatime
            object_config.save()



def run_sync_cms_db():
    p = TSyncConfig.objects.all()
    for object_config in p:
        get_configInfo(object_config)







