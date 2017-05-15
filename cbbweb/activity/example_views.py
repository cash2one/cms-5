# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.

# example
def girl(request, *args, **kwargs):
    return render(request, 'activity/example/base.html')

def vest(request, *args, **kwargs):
    return render(request, 'activity/example/vest.html')

def skirt(request, *args, **kwargs):
    return render(request, 'activity/example/skirt.html')

