# -*- coding: utf-8 -*-

import logging
import json

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404

from cbbweb.cms import models as cmsmodels
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils import (str2array, to_dict, get_method_dict)
from cbbweb.core.utils import db
from cbbweb.core.utils.modelname import ModelName
from cbbweb.service import (list_objs)

logger = logging.getLogger('service')

@redis_func()
def get_product_image_type_dict():
    '''
    获取所有图片类别ID和对应的名称
    '''

    sql = """
    SELECT
        b.DICT_KEY,
        b.DICT_VALUE
    FROM
        t_base_data_dict_group a
    LEFT JOIN t_base_data_dict b ON a.ID = b.DICTGROUP_ID
    WHERE
        a.DICTGROUP_NAME = 'carImageType'
    ORDER BY
        b.SORT_ORDER ASC
    """

    return db.fetch(sql)


@redis_func()
def get_product_images(series_id=None, model_id=None, position=None, countofpage=0, pagecount=0):
    '''
    获取所有图片列表
    @param series_id 车系ID，必填，以下为非必填项
    @param model_id 车型ID
    @param position 位置代码，代码对应中文请调用 get_product_image_type_dict 接口获取
    @param countofpage 每页图片个数
    @param pagecount 页码
    @return 返回以上条件下的所有图片，返回的字段参照 t_base_product_image 表字段定义
    '''

    sql = """
    SELECT
        *
    FROM
        t_base_product_image
    WHERE
    	CAR_SERIES_ID = """

    if not series_id or int(series_id) <= 0: return None

    sql += series_id

    if model_id and int(model_id) > 0: sql += " AND CAR_MODEL_ID = %s" % model_id

    if position and int(position) > 0: sql += " AND POSITION = %s" % position

    if not countofpage or int(countofpage) <= 0: countofpage = 8
    if not pagecount or int(pagecount) <= 0: pagecount = 0
    sql += " LIMIT %s, %s" % (int(pagecount) * int(countofpage), countofpage)

    tmp = db.fetch(sql)

    return tmp
