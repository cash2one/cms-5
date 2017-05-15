# -*- coding: utf-8 -*-

import datetime
import json
import requests
from django.conf import settings
from django.utils import timezone
from cbbweb.core.models import TClueInfo
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import get_object
from cbbweb.service.cms_utils import common_utils

sqlField = {'id': '',
            'auth_key':'authKey',
            'action_type':'actionType',
            'name':'name',
            'phone':'phone',
            'store_id':'storeId',
            'clue_type':'clueType',
            'source':'source',
            'car_type_id':'carTypeId',
            'car_series_id':'carSeriesId',
            'sex':'sex',
            'dlr_code':'dlrCode',
            'address':'address',
            'province_id':'provinceId',
            'city_id':'cityId',
            'activity_id':'activityId',
            'activity_name':'activityName',
            'county_id':'countyId',
            'smart_code':'smartCode',
            'page_id':'pageId',
            'created_date':'',
            'result_json':'',
            'status_code':'',
            'kwargs_json':''}

def get_clue_save_api(**kwargs):
   
    if 'actionType' not in kwargs:
        kwargs['actionType'] = 'saveClue'
 
    if 'authKey' not in kwargs:
        kwargs['authKey'] = 'abc123!!'

    if 'source' not in kwargs:
        kwargs['source'] = '4'

    if 'clueType' not in kwargs:
        kwargs['clueType'] = '6'

    into_sqlFieldname = []
    into_sqlField = [] 
    kwargs_json = json.dumps(kwargs, ensure_ascii=False)

    if 'carTypeId' in kwargs:
        if kwargs['carTypeId']:
            car_type_id = common_utils.to_int(kwargs['carTypeId'])
            car_type = get_object(model=ModelName.T_BASE_CAR_TYPE,
                                  is_enable=1, is_show=1,
                                  id=car_type_id)
            if car_type:
                kwargs['carTypeId'] = car_type.e4s_car_type_id

    if 'carSeriesId' in kwargs:
        if kwargs['carSeriesId']:
            car_series_id = common_utils.to_int(kwargs['carSeriesId'])
            car_series = get_object(model=ModelName.T_BASE_CAR_SERIES,
                                    is_enable=1, is_show=1,
                                    id=car_series_id)    
            if car_series:

                kwargs['carSeriesId'] = car_series.mdm_car_series_id

    
    for key in kwargs:
        for k in sqlField:
            if key == sqlField[k]:
                into_sqlFieldname.append(k)
                into_sqlField.append(kwargs[key])


    now_time = datetime.datetime.now()

    into_sqlFieldname.append('kwargs_json')
    into_sqlFieldname.append('created_date')
    into_sqlField.append(kwargs_json)
    into_sqlField.append(now_time)
    tmp_dict = {
        'action_type': 'saveClue',
        'auth_key': 'abc123!!',
        'source': '4',
        'clue_type': '6',
    }
    for i in range(len(into_sqlFieldname)):
        tmp_dict[into_sqlFieldname[i]] = into_sqlField[i]  
    q = TClueInfo(**tmp_dict)
    q.save() 




    
    for k in kwargs:
        kwargs[k] = kwargs[k].encode('gbk')

    api_address = 'http://e4s.stg.dongfeng-nissan.com.cn/ajax/leaveInfo/cbbLeaveInfo.do'
    if not settings.DEBUG: 
        api_address = 'http://www.chebaba.com/ajax/leaveInfo/cbbLeaveInfo.do'

    flag = requests.post(api_address, data=kwargs)  
    status_code = flag.status_code
    t_dict = None
    if status_code == 200:
        content = flag.text
        try:
            t_dict = json.loads(content) 
        except:
            t_dict = {}
    q.status_code = status_code
    q.result_json = t_dict
    q.save()           

    return flag.text

