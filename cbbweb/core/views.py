# -*- coding: utf-8 -*-


from django.views.generic import View
from django.shortcuts import render
from cbbweb.core.utils.constants import API
from cbbweb.core.utils import is_mobile
from cbbweb.core.utils.rediscache import redis_func
from cbbweb.core.utils.modelname import ModelName
from cbbweb.core.utils.views import init_context


STATUS_ERROR = "error"
STATUS_SUCCESS = "success"


def index(request, *args, **kwargs):
    return render(request, 'base/base.html')


class CbbView(View):
    '''
        Base View for Cbb
    '''

def handler500(request, *args, **kwargs):
    context = init_context()

    mobile_flag = is_mobile(request.META['HTTP_USER_AGENT'])
    if mobile_flag:
        return render(request, 'wap/site/error/502.html', context)
    else:
        return render(request, 'site/breakdown500.html', context)


def handler404(request, *args, **kwargs):
    context = init_context()

    mobile_flag = is_mobile(request.META['HTTP_USER_AGENT'])
    if mobile_flag:
        return render(request, 'wap/site/error/404.html', context)
    else:
        return render(request, 'site/notfound.html', context)
