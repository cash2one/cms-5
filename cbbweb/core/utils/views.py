# -*- coding: utf-8 -*-
from django.views.generic.base import ContextMixin
from django.views.generic import View
from django.shortcuts import render

from cbbweb.core.utils import (is_mobile, app_local_data)
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.constants import API

from django.conf import settings

def init_context():
    return {
        'API': API,
        'MODELS': ModelName,
        'city': app_local_data.city,
        'DEBUG': settings.DEBUG
    }

class CbbBaseView(ContextMixin, View):

    def get_context_data(self, request, **kwargs):
        context = super(CbbBaseView, self).get_context_data(**kwargs)
        context['API'] = API
        context['MODELS'] = ModelName
        context['city'] = app_local_data.city
        return context


class CbbTemplateView(CbbBaseView):

    pc_template = None
    wap_template = None

    def get_service_data(self, request, context, **kwargs):
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(request, **kwargs)
        context = self.get_service_data(request, context, **kwargs)

        mobile_flag = is_mobile(request.META['HTTP_USER_AGENT'])
        if mobile_flag:
            return render(request, self.wap_template, context)
        else:
            return render(request, self.pc_template, context)
