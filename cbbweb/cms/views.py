# -*- coding: utf-8 -*-

import re
from django.shortcuts import render
from django.core.urlresolvers import resolve, Resolver404
from django.http import Http404

from cbbweb.cms.models import TCmsCataAttrs, TCmsCatalogs
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb import service
from cbbweb.core.utils.constants import API
from cbbweb.core.utils import is_mobile
from django.conf import settings
import logging
from cbbweb.core.utils.views import (init_context)
from cbbweb.service.cms_utils import car_series_utils

logger = logging.getLogger("cms")

SLASH = '/'


def article(request, id, *args, **kwargs):
    '''
        read article
        two default data
        ===============
        INSERT INTO `t_cms_template` (`id`,`template_name`,`template_path`,`creator`,`created_date`,`modifier`,`update_date`,`template_type`,`template_teriminal`) VALUES (1,'默认模板','wap/site/car/news.html','admin','2016-01-13 18:59:11','admin','2016-01-13 18:59:11','ARTICLE','PC');
        INSERT INTO `t_cms_template` (`id`,`template_name`,`template_path`,`creator`,`created_date`,`modifier`,`update_date`,`template_type`,`template_teriminal`) VALUES (2,'默认模板','wap/site/car/news.html','admin','2016-01-21 14:17:34','admin','2016-01-21 14:17:40','ARTICLE','WAP');
        ===============
    '''
    ids = id.split('_')
    article_id = ids[0]
    cur_page = 1
    if len(ids) == 2:
        try:
            cur_page = int(ids[1])
        except:
            raise Http404

    mobile_flag = is_mobile(request.META['HTTP_USER_AGENT'])

    # fetch data
    article = service.get_object(model=ModelName.T_CMS_ARTICLE,
                                 id=article_id)
    if not article:
        raise Http404

    section = service.get_object(model=ModelName.T_CMS_SECTION,
                                 id=article.section_id)
    template_id = (section.mobile_template_id
                   if mobile_flag else section.pc_template_id)
    template = service.get_object(model=ModelName.T_CMS_TEMPLATE,
                                  id=template_id)
    article_rela = service.list_objs(model=ModelName.T_CMS_ARTICLE_RELA,
                                     article_id=article.id, type='CAR_SERIES',
                                     exclude={'status':'DEL'})

    # car_series_ids = [rela.object_id for rela in article_rela]
    car_series_ids = []
    for tmp_rela in article_rela:
        tmp_car_series_id = tmp_rela.object_id
        tmp_car_series = car_series_utils.get_carseries_by_id(
            car_series_id=tmp_car_series_id
        )
        if tmp_car_series:
            car_series_ids.append(tmp_car_series['id'])


    content = article.trans_content

    # split the page code
    content_split =re.split(u'\[#([\u4E00-\u9FA5a-zA-Z0-9]*)#\]', content)

    # calc max_page
    max_page = 1
    if len(content_split) > 1:
        max_page = int((len(content_split)-1)/2)

    if cur_page > max_page :
        raise Http404

    # handle content
    finalContent = [];
    if mobile_flag:
        # mobile, return all content
        for i in range(max_page):
            finalContent.append(content_split[i*2])
    else:
        # pc, if cur_page==0, return all content
        # else return the page content
        if cur_page == 0:
            for i in range(max_page):
                finalContent.append(content_split[i*2])
        else:
            finalContent.append(content_split[(cur_page-1)*2])

    article.trans_content = "".join(finalContent)

    context = init_context()
    context.update({
        'article':article,
        'car_series_ids':car_series_ids,
        'section':section,
        'paginator':{
            'num_pages':max_page,
            'cur_page':cur_page
        }
    })

    if mobile_flag:
        return render(request, template.template_path, context)
    else:
        return render(request, template.template_path, context)


def parse_alias(request, *args, **kwargs):
    '''
        parse all catalogs
    '''

    logger.info("url access: %s, ua: %s" %
                (request.get_full_path(), request.META['HTTP_USER_AGENT']))
    full_path = clean_full_path(request)
    mobile_flag = is_mobile(request.META['HTTP_USER_AGENT'])

    catalogs = get_catalogs(full_path)
    if catalogs:
        context = pre_setup_context(request, catalogs)
        cata_full_alias = catalogs.cata_full_alias

        if cata_full_alias == full_path:
            if mobile_flag:
                logger.info("use template: %s" % (catalogs.mobile_template))
                return render(request, catalogs.mobile_template, context)
            else:
                logger.info("use template: %s" % (catalogs.pc_template))
                return render(request, catalogs.pc_template, context)

        elif full_path.startswith(cata_full_alias):
            sub_id = full_path[len(cata_full_alias)+1:]
            context['sub_id'] = sub_id
            if mobile_flag:
                logger.info("use template: %s" %
                            (catalogs.mobile_content_template))
                return render(request,
                              catalogs.mobile_content_template, context)
            else:
                logger.info("use template: %s" %
                            (catalogs.pc_content_template))
                return render(request,
                              catalogs.pc_content_template, context)
        else:
            raise Http404
            # real_url = city_code + full_path[len(alias_url)-1:]
            # try:
            #     view, args, kwargs = resolve(real_url)
            # except Resolver404:
            #     raise Http404
            # if view == parse_alias:
            #     raise Http404
            # kwargs['request'] = request
            # return view(*args, **kwargs)
    raise Http404


def pre_setup_context(request, catalogs):

    context = init_context()
    context['catalogs'] = catalogs

    cata_attrs = {}
    cata_attrs_list = get_cata_attrs_list(catalogs.id)
    for cata_attr in cata_attrs_list:
        cata_attrs[cata_attr.enname] = cata_attr
    context['cata_attrs'] = cata_attrs

    if catalogs.model_table != '':
        _model_name = getattr(ModelName, catalogs.model_table.upper())
        kwargs = {}
        kwargs['model'] = _model_name
        kwargs['id'] = catalogs.model_instanceid
        kwargs['is_enable'] = 1
        cata_model = service.get_object(**kwargs)
        context['cata_model'] = cata_model

    return context

def clean_full_path(request):
    city_code = SLASH + request.GET.get('citycode')
    citycode_len = len(city_code)
    full_path = request.get_full_path()[citycode_len:]

    qIdx = full_path.find('?')
    if(qIdx != -1):
        full_path = full_path[:qIdx]

    return full_path.rstrip(SLASH)


def get_catalogs(full_path):
    catalogs = service.get_object(model=ModelName.T_CMS_CATALOGS,
                                  is_enable=1,
                                  cata_full_alias=full_path)
    if catalogs:
        return catalogs
    else:
        try:
            sub_slash_index = full_path[:-1].rindex(SLASH)
        except ValueError:
            return None
        sub_alias = full_path[: sub_slash_index]
        if sub_alias in ['', '/']:
            logger.warn("the root path no need to find.")
            return None

        catalogs = service.get_object(model=ModelName.T_CMS_CATALOGS,
                                      is_enable=1,
                                      cata_full_alias=sub_alias)
        return catalogs if catalogs else None



@redis_func()
def get_cata_attrs_list(cata_id):
    cata_attrs_list = service.list_objs(model=ModelName.T_CMS_CATA_ATTRS,
                                        cata_id=cata_id)
    return cata_attrs_list
