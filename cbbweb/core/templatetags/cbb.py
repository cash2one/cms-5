# -*- coding: utf-8 -*-
from django import template
from cbbweb.base.utils.tag import (url_tag_parser, CityURLNode)

register = template.Library()


@register.tag
def city_url(parser, token):
    viewname, args, kwargs, asvar = url_tag_parser(parser, token)
    return CityURLNode(viewname, args, kwargs, asvar)



