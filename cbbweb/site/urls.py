# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name="site.index"),
    url(r'^config/(?P<id>[\w-]+)$', views.CarConfigView.as_view(),
        name="site.car_type_param"),
    url(r'^activity/dealer/(?P<activity_type>[\w-]+)/(?P<yyyymm>[\w-]+)/(?P<activity_id>[\w-]+)[/]{0,1}$',
        views.DealerActivityView.as_view(), name="site.dealer_activity"),

    url(r'^photo/(?P<series_id>[\w-]+)/$', views.ProductImageView.as_view(), name='site.product_image_series'),
    url(r'^photo/(?P<series_id>[\w-]+)/(?P<model_id>[\w-]+)$', views.ProductImageView.as_view(), name='site.product_image_series_model'),
    url(r'^finance_detail/(?P<series_id>[\w-]+)$', views.FinanceDetailView.as_view(), name='site.finance_detail'),
    url(r'^finance_detail/(?P<series_id>[\w-]+)/(?P<model_id>[\w-]+)$', views.FinanceDetailView.as_view(), name='site.finance_detail_model'),


    # 金融留资
    url(r'^finance/apply$', views.FinanceApplyView.as_view(), name='site.finance_apply'),
    url(r'^finance/complete$', views.FinanceApplyComplete.as_view(), name='site.finance_complete'),
    url(r'^finance/done$', views.FinanceApplyDone.as_view(), name='site.finance_done'),

    url(r'^checkloan$', views.CheckloanView.as_view(), name="site.checkloan"),

    # 通用留资
    url(r'^info/apply$', views.InfoApplyView.as_view(), name="site.left_data"),
    url(r'^info/complete$', views.InfoCompleteView.as_view(), name="site.perfect_data"),
    url(r'^info/done$', views.InfoDoneView.as_view(), name="site.left_done"),

    url(r'^html/(?P<template_path>.*)', views.handle_static_html, name="site.handle_static_html"),

)
