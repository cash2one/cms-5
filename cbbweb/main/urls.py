# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    # url(r'^$', views.MainView.as_view(), name="main_index"),
    # url(r'^$', views.index, name="main_index"),
    url(r'^hui/$', views.hui, name='main_hui'),

    url(r'^hui/(?P<seq>[\w-]+)/$', views.hui, name='main_hui_detail'),
)
