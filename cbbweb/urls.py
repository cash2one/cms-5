# -*- coding: utf-8 -*-
"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.conf import settings
from django.contrib import admin
from django.views.generic import TemplateView

# from django.views.decorators.cache import cache_page

from cbbweb.cms import views as cmsviews
from cbbweb.service import views as serviceviews

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #baidu_verify_jsAXHU5kpk.html

    url(r'^(?P<citycode>[\w-]+)/', include([

        url(r'^', include('cbbweb.main.urls')),

        url(r'^baidu_verify_jsAXHU5kpk\.html$',
            TemplateView.as_view(template_name="site/baidu_verify_jsAXHU5kpk.html")),

        # site url
        url(r'^', include('cbbweb.site.urls')),

        # api
        url(r'^api/(?P<service_name>[\w_]+)/', serviceviews.rest,
            name='cbbweb.rest'),

        # article
        url(r'article/(?P<id>[\w-]+)', cmsviews.article , name='cms.article'),
        # parse alias
        url(r'(?P<catalog_url>.*)', cmsviews.parse_alias, name='parse_alias'),
        # url(r'(?P<catalog_url>.*)', cache_page(60 * 15)(cmsviews.parse_alias), name='parse_alias'),
    ])),
]

handler500 = 'cbbweb.core.views.handler500'
handler404 = 'cbbweb.core.views.handler404'
