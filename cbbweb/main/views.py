# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.conf import settings
from django.views.generic import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'base/base.html',  {"settings":settings})


# def index(request):
#     return render(request, 'base/base.html')

def hui(request, *args, **kwargs):
    return render(request, 'site/hui.html',  {"settings":settings})
