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
def get_article_detail_with_series(article_id=0):
    '''
    根据ID获取一篇文章的详细内容，包含车系ID
    @param article_id 文章ID
    @return 返回一条文章的详细内容以及车系详情
    '''
    if not article_id or int(article_id) <= 0: return None

    sql = """
    SELECT
        id,
        title,
        keywords,
        front_img_path,
        source,
        description,
        content,
        created_date,
        '' series
    FROM
        t_cms_article
    WHERE
        `status` = 'PUBLISH' AND id = %(article_id)s
    LIMIT 1
    """

    params = {}
    params['article_id'] = article_id

    tmp = db.fetchone(sql, params)
    if not tmp or len(tmp) == 0: return None

    sql = """
    SELECT
        a.object_id,
        b.CAR_SERIES_CN,
        b.START_GUIDEPRICE,
        b.WAP_THUMBNAIL,
        b.PC_THUMBNAIL
    FROM
        t_cms_article_rela a
    LEFT JOIN t_base_car_series b ON a.object_id = b.ID
    WHERE
        a.article_id = %(article_id)s
        AND a.status != 'DEL'
    GROUP BY
        a.object_id
    """

    tmp['series'] = db.fetch(sql, params)
    return tmp


@redis_func()
def get_article_newest_by_carseries(series_id=0, count=1, page=0):
    '''
    根据车系ID，获取最新相关文章，一条和多条
    @param series_id 车系ID
    @param count 获取最新文章条数，不传入默认为1
    @param page 页数，为0时不分页，否则表示具体页码
    @return 返回最新一条相关文章的基本信息，按日期降序排列
    '''
    if not series_id or int(series_id) <= 0: return None

    sql = """
    SELECT
        b.id,
        b.title,
        b.front_img_path,
        a.object_id,
        a.object_name,
        a.created_date,
        a.update_date
    FROM
        t_cms_article_rela a
    LEFT JOIN t_cms_article b ON a.article_id = b.id
    WHERE
        a.object_id = %(series_id)s
        AND a.status != 'DEL'
        AND b.`status` = 'PUBLISH'
    ORDER BY
        b.created_date DESC
    LIMIT %(page)s, %(count)s
    """

    params = {}
    params['series_id'] = series_id

    if not count or int(count) <= 1: params['count'] = 1
    else: params['count'] = int(count)

    if not page or int(page) <= 1: params['page'] = 0
    else: params['page'] = (int(page) - 1) * int(count)

    return db.fetch(sql, params)


@redis_func()
def get_article_brief_with_series(series_id=0, count=1, page=0):
    '''
    获取用于瀑布流式显示的文章列表，只包含基本信息
    @param series_id 车系ID
    @param count 获取最新文章条数，不传入默认为1
    @param page 页数，为0时不分页，否则表示具体页码
    @return 返回最新多条文章
    '''
    sql = """
    SELECT
        a.article_id,
        b.front_img_path,
        b.title,
        b.source,
        b.created_date,
        b.description
    FROM
        t_cms_article_rela a
    LEFT JOIN t_cms_article b ON a.article_id = b.id
    WHERE
        a.object_id = %(series_id)s
    AND a.status != 'DEL'
    AND b.`status` = 'PUBLISH'
    ORDER BY
        b.created_date DESC
    LIMIT %(page)s, %(count)s
    """

    params = {}
    params['series_id'] = series_id

    if not count or int(count) <= 1: params['count'] = 1
    else: params['count'] = int(count)

    if not page or int(page) <= 1: params['page'] = 0
    else: params['page'] = (int(page) - 1) * int(count)

    return db.fetch(sql, params)
