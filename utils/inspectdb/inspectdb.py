#!/usr/bin/env python

# -*- coding: utf-8 -*-


import sys
import os
import django

from django.core.management.commands.inspectdb import Command

sys.path.append('../..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbbweb.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

import configurations
configurations.setup()

TABLE_NAME_LIST = [
    # cms
    't_cms_cata_attrs',
    't_cms_catalogs',

    # base_dealer
    't_base_dealer',
    't_base_dealer_mdm',
    't_base_employee',

    # base_car
    't_base_car_brand',
    't_base_car_brand_mdm',
    't_base_car_color',
    't_base_car_incolor',
    't_base_car_series',
    't_base_car_series_mdm',
    't_base_car_type',
    't_base_car_type_property',
    't_base_car_type_property_template',
    't_base_large_car_type',
    't_base_middle_car_type',
    't_base_small_car_type',

    # base_area
    't_base_bigarea',
    't_base_city',
    't_base_county',
    't_base_province',
    't_base_region',
    't_base_smallarea',

    # base_financial
    't_base_financial_condition_rel',
    't_base_financial_corp',
    't_base_financial_dlr_rel',
    't_base_financial_feature_rel',
    't_base_financial_first_pay_percent_rel',
    't_base_financial_material_rel',
    't_base_financial_pro_sku',
    't_base_financial_product',
    't_base_financial_series_rel',

    # base_price
    't_base_car_series_mapping',
    't_base_car_type_mapping',
    't_base_dealer_mapping',
    't_base_offer_price',

]

Command().execute(
    table_name_filter=lambda table_name: table_name in TABLE_NAME_LIST, 
    database='cms'
)

