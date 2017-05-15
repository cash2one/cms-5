# -*- coding: utf-8 -*-

import logging
import requests

from django.conf import settings
from cbbweb.core.utils import trace_log


logger = logging.getLogger('service')

SEND_VERIFY_CODE_API = settings.SMS_URL \
    + "/sms-service/sms/mess/sendsms?mobile=%s&clientIp=%s"

VERIFY_CODE_API = settings.SMS_URL \
    + "/sms-service/sms/mess/verifyCode?mobile=%s&verifyCode=%s"

DEFAULT_RESULT = {"retnCode": "0", "retnDesc": None, "results": None}
ERROR_RESULT = {"retnCode": "-999", "retnDesc": None, "results": None}


def send_verify_code(mobile, ip):
    '''
        fetch phone verify code
    '''
    rtn = dict(ERROR_RESULT)
    msg = _valid_phone(mobile)
    if msg:
        rtn['retnDesc'] = msg
        return rtn
    url = SEND_VERIFY_CODE_API % (mobile, ip)
    logger.info("send verify code message, request url: %s", url)
    res = requests.get(url)
    try:
        res_content = res.json()
        return res_content
    except:
        logger.error(trace_log('SEND_VERIFY_CODE_API result parse json error'))
        return DEFAULT_RESULT


def verify_code(mobile, verify_code):
    '''
        fetch phone verify code
    '''
    rtn = dict(ERROR_RESULT)
    msg = _valid(mobile=mobile, code=verify_code)
    if msg:
        rtn['retnDesc'] = msg
        return rtn

    res = requests.get(VERIFY_CODE_API % (mobile, verify_code))
    try:
        res_content = res.json()
        return res_content
    except:
        logger.error(trace_log('VERIFY_CODE_API result parse json error'))
        return DEFAULT_RESULT


def _valid_phone(mobile):
    if not mobile:
        return u'手机号码不能为空'

    if len(mobile.strip()) != 11:
        return u'手机号码不正确'

    return None


def _valid_verify_code(code):
    if len(code.strip()) != 4:
        return u'验证码不正确'

    return None


def _valid(mobile=None, code=None):
    msg = _valid_phone(mobile)
    return msg if msg else _valid_verify_code(code)
