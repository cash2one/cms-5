from django.conf.urls import include, patterns, url
from . import example_views

urlpatterns = [

    url(r'^example/', include([
        url(r'^$', example_views.girl, name='activity.girl'),
        url(r'^vest/$', example_views.vest, name='activity.vest'),
        url(r'^skirt/$', example_views.skirt, name='activity.skirt'),
    ])),

]
