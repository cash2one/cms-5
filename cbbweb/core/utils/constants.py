# -*- coding: utf-8 -*-

from enum import Enum

CORE_SERVICE = 'cbbweb.service'
ARTICLE_SERVICE = 'cbbweb.service.article_service'  # Tom
DEALER_SERVICE = 'cbbweb.service.dealer_service'
CAR_SERVICE = 'cbbweb.service.car_service'
FINANCIAL_SERVICE = 'cbbweb.service.financial_service'  # Tom
CATALOGS_SERVICE = 'cbbweb.service.catalogs_service'
PRODUCT_SERVICE = 'cbbweb.service.product_service'  # Tom
AREA_SERVICE = 'cbbweb.service.area_service'
CLUE_SERVICE = 'cbbweb.service.clue_service'  # Tom
SMS_SERVICE = 'cbbweb.service.sms_service'

class API(Enum):
    GET = (CORE_SERVICE, 'get_object')
    LIST = (CORE_SERVICE, 'list_objs')
    COUNT = (CORE_SERVICE, 'count_objs')
    PAGE = (CORE_SERVICE, 'get_paginator')

    GET_REST = (CORE_SERVICE, 'get_object_rest')
    LIST_REST = (CORE_SERVICE, 'list_objs_rest')
    COUNT_REST = (CORE_SERVICE, 'count_objs_rest')
    PAGE_REST = (CORE_SERVICE, 'get_paginator_rest')

    # ARTICLE_SERVICE START
    ARTICLE_NEWEST_BY_CARSERIES = (ARTICLE_SERVICE, 'get_article_newest_by_carseries')
    ARTICLE_DETAIL_WITH_SERIES = (ARTICLE_SERVICE, 'get_article_detail_with_series')
    ARTICLE_BRIEF_WITH_SERIES = (ARTICLE_SERVICE, 'get_article_brief_with_series')
    # ARTICLE_SERVICE END

    # FINANCIAL SERVICE START
    LOWEST_DOWNPAY_MONTHLY = (FINANCIAL_SERVICE, 'get_lowest_downpay_monthly')
    DOWNPAY_MONTHLY_COUNT = (FINANCIAL_SERVICE, 'get_downpay_monthly_count')
    LOWEST_SUMMARY = (FINANCIAL_SERVICE, 'get_lowest_summary')
    DOWNPAYS = (FINANCIAL_SERVICE, 'get_downpays')
    PERIODS = (FINANCIAL_SERVICE, 'get_periods')
    PURCHASETAX_TOTALFEE = (FINANCIAL_SERVICE, 'get_purchasetax_totalfee')
    FINANCIALS = (FINANCIAL_SERVICE, 'get_financials')
    # 根据城市、车系，获取最低月供的金融方案
    LOWEST_MONTHLY_PAYMENT = (FINANCIAL_SERVICE, 'get_lowest_monthly_payment')
    # 获取金融相关包装数据
    FINANCIAL_PACK_DATA = (FINANCIAL_SERVICE, 'get_financial_pack_data')
    LIST_FINANCIALS = (FINANCIAL_SERVICE, 'list_financials')
    INTEREST_CALC = (FINANCIAL_SERVICE, 'interest_calc')
    PURCHASETAX = (FINANCIAL_SERVICE, 'get_purchasetax')
    CARTYPE_TAX_INSURANCE = (FINANCIAL_SERVICE, 'get_cartype_tax_insurance')

    # 征信接口
    CREDIT_DNAF_SAVE = (FINANCIAL_SERVICE, 'get_credit_dnaf_save')
    CREDIT_DNAF_QUERY = (FINANCIAL_SERVICE, 'get_credit_dnaf_query')
    CREDIT_CMBC_SAVE = (FINANCIAL_SERVICE, 'get_credit_cmbc_save')
    CREDIT_CMBC_QUERY = (FINANCIAL_SERVICE, 'get_credit_cmbc_query')
    # FINANCIAL SERVICE END

    # PRODUCT_SERVICE START
    PRODUCT_IMAGE_TYPE_DICT = (PRODUCT_SERVICE, 'get_product_image_type_dict')
    PRODUCT_IMAGES = (PRODUCT_SERVICE, 'get_product_images')
    # PRODUCT_SERVICE END

    # CATALOGS SERVICE START
    CATALOG_URL = (CATALOGS_SERVICE, 'get_catalog_url')
    SEARCH_RESULT = (CATALOGS_SERVICE, 'get_search_result')
    # CATALOGS SERVICE END


    # AREA SERVICE START
    CITY_DATA = (AREA_SERVICE, 'get_city_data')
    HOT_CITY = (AREA_SERVICE, 'get_hot_city')
    DIRECT_CITY = (AREA_SERVICE, 'get_city_data')
    # AREA SERVICE END







    # API BY PAGE START <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    # CAR #############################
    CAR_BRAND_BY_ID = ('cbbweb.service.page.car.car_api',
                       'get_car_brand_by_id')
    CAR_BRAND_LIST_BY_ID = ('cbbweb.service.page.car.car_api',
                            'get_car_brand_list_by_id')
    CAR_OFFICAL_CAR_INFO = ('cbbweb.service.page.car.car_api',
                            'get_car_offical_car_info')
    CAR_CATALOG_DATA = ('cbbweb.service.page.car.car_api',
                        'get_car_catalog_data')
    CAR_CATALOG_BRAND_DATA = ('cbbweb.service.page.car.car_api',
                              'get_car_catalog_brand_data')
    CAR_ARTICLE_INFO = ('cbbweb.service.page.car.car_api',
                        'get_car_article_info')


    # CAR SERIES ######################
    CAR_SERIES_BY_ID = ('cbbweb.service.page.car_series.car_series_api',
                        'get_car_series_by_id')
    CAR_SERIES_DATA = ('cbbweb.service.page.car_series.car_series_api',
                       'get_car_series_data')
    CAR_SERIES_PROPERTY = ('cbbweb.service.page.car_series.car_series_api',
                           'get_car_series_property')
    # replace : HOT_CAR_SERIES
    CAR_SERIES_HOT = ('cbbweb.service.page.car_series.car_series_api',
                      'get_hot_car_series')
    # replace : ON_SALE_CAR_TYPES
    CAR_SERIES_ON_SALE_CAR_TYPES = ('cbbweb.service.page.car_series.car_series_api',
                                    'get_on_sale_car_types')
    CAR_SERIES_DEALER = ('cbbweb.service.page.car_series.car_series_api',
                         'get_car_series_dealer')
    # replace : GROUP_SERIES_CAR_TYPES
    CAR_SERIES_GROUP_CAR_TYPES = ('cbbweb.service.page.car_series.car_series_api',
                                  'get_group_series_car_types')
    CAR_SERIES_SEARCH = ('cbbweb.service.page.car_series.car_series_api',
                         'get_car_series_search')

    # dep --- CAR_SERIES_HOT
    HOT_CAR_SERIES = ('cbbweb.service.page.car_series.car_series_api',
                      'get_hot_car_series')
    # dep --- CAR_SERIES_ON_SALE_CAR_TYPES
    ON_SALE_CAR_TYPES = ('cbbweb.service.page.car_series.car_series_api',
                         'get_on_sale_car_types')
    # dep --- CAR_SERIES_GROUP_CAR_TYPES
    GROUP_SERIES_CAR_TYPES = ('cbbweb.service.page.car_series.car_series_api',
                              'get_group_series_car_types')

    # CAR TYPE #############################
    CAR_TYPE_BY_ID = ('cbbweb.service.page.car_type.car_type_api',
                      'get_car_type_by_id')
    CAR_TYPE_DATA = ('cbbweb.service.page.car_type.car_type_api',
                     'get_car_type_data')
    CAR_TYPE_PROPERTY = ('cbbweb.service.page.car_type.car_type_api',
                         'get_car_type_property')
    CAR_TYPE_GROUP_PROPERTY = ('cbbweb.service.page.car_type.car_type_api',
                               'get_car_type_group_property')
    CAR_TYPE_ALL_PROPERTY = ('cbbweb.service.page.car_type.car_type_api',
                             'get_car_type_all_property')
    CAR_TYPE_DEALER = ('cbbweb.service.page.car_type.car_type_api',
                       'get_car_type_dealer')
    # replace : CITY_CAR_TYPE_DEALER_COUNT
    CAR_TYPE_CITY_DEALER_COUNT = ('cbbweb.service.page.car_type.car_type_api',
                                  'get_city_car_type_dealer_count')
    CAR_TYPES_BY_CAR_SERIES_ID = ('cbbweb.service.page.car_type.car_type_api',
                                  'get_car_types_by_car_series_id')
    CAR_TYPE_PRICE_PROPERTY = ('cbbweb.service.page.car_type.car_type_api',
                               'get_car_type_price_property')
    CAR_TYPE_SERIES_PRICE_PROPERTY = ('cbbweb.service.page.car_type.car_type_api',
                                      'get_car_type_series_price_property')

    # dep --- CAR_TYPE_CITY_DEALER_COUNT
    CITY_CAR_TYPE_DEALER_COUNT = ('cbbweb.service.page.car_type.car_type_api',
                                  'get_city_car_type_dealer_count')

    # DEALER ################################
    DEALER_BY_ID = ('cbbweb.service.page.dealer.dealer_api',
                    'get_dealer_by_id')
    DEALER_DEFAULT = ('cbbweb.service.page.dealer.dealer_api',
                      'get_dealer_by_default')
    DEALER_SCORE = ('cbbweb.service.page.dealer.dealer_api',
                    'get_dealer_by_score')
    DEALER_DISTANCE = ('cbbweb.service.page.dealer.dealer_api',
                       'get_dealer_by_distance')
    DEALER_ON_SALE_CAR_TYPES = ('cbbweb.service.page.dealer.dealer_api',
                                'get_dealer_on_sale_car_types')
    DEALER_ON_SALE_CAR_TYPES_COUNT = ('cbbweb.service.page.dealer.dealer_api',
                                      'get_dealer_on_sale_car_types_count')
    DEALER_GROUP_SERIES_CAR_TYPES = ('cbbweb.service.page.dealer.dealer_api',
                                     'get_dealer_group_series_car_types')
    DEALER_ACTIVITY_SERIES_CAR_TYPES = ('cbbweb.service.page.dealer.dealer_api',
                                        'get_dealer_activity_series_car_types')
    DEALER_CAR_SERIES_PROPERTY = ('cbbweb.service.page.dealer.dealer_api',
                                  'get_dealer_car_series_property')
    DEALER_HOT_CAR_SERIES = ('cbbweb.service.page.dealer.dealer_api',
                             'get_dealer_hot_car_series')
    DEALER_PROMOTION_ACTIVITY = ('cbbweb.service.page.dealer.dealer_api',
                                 'get_dealer_promotion_activity')
    DEALER_CITY_ACTIVITY = ('cbbweb.service.page.dealer.dealer_api',
                            'get_dealer_city_activity')
    DEALER_OFFICAL_CAR_INFO = ('cbbweb.service.page.dealer.dealer_api',
                               'get_dealer_offical_car_info')


    # FINANCE ######################################
    # replace : GROUP_BRAND_CAR_SERIES
    FINANCE_GROUP_BRAND_CAR_SERIES = ('cbbweb.service.page.finance.finance_api',
                                      'get_group_brand_car_series')
    FINANCE_CAR_TYPE_DEALER = ('cbbweb.service.page.finance.finance_api',
                               'get_finance_car_type_dealer')
    FINANCE_CAR_SERIES_CAR_TYPE = ('cbbweb.service.page.finance.finance_api',
                                   'get_finance_car_series_car_type')
    FINANCE_CAR_SERIES_AND_CAR_TYPE = ('cbbweb.service.page.finance.finance_api',
                                       'get_finance_car_series_and_car_type')
    FINANCE_CAR_SERIES_PROVINCE_INFO = ('cbbweb.service.page.finance.finance_api',
                                        'get_finance_car_series_province_info')
    FINANCE_CAR_SERIES_CITY_INFO = ('cbbweb.service.page.finance.finance_api',
                                    'get_finance_car_series_city_info')
    FINANCE_CAR_SERIES_COUNTY_INFO = ('cbbweb.service.page.finance.finance_api',
                                      'get_finance_car_series_county_info')
    FINANCE_CAR_SERIES_LIST = ('cbbweb.service.page.finance.finance_api',
                               'get_finance_car_series_list')
    FINANCE_CITY_BRAND_DEALER = ('cbbweb.service.page.finance.finance_api',
                                 'get_finance_city_brand_dealer')
    FINANCE_COUNTY_BRAND_DEALER = ('cbbweb.service.page.finance.finance_api',
                                   'get_finance_county_brand_dealer')
    FINANCE_GROUP_SERIES_CAR_TYPES = ('cbbweb.service.page.finance.finance_api',
                                      'get_finance_group_series_car_types')
    FINANCE_DEALER_CAR_TYPES_PRICE = ('cbbweb.service.page.finance.finance_api',
                                      'get_finance_dealer_car_types_price')
    FINANCE_PROVINCE_CITY_COUNTY = ('cbbweb.service.page.finance.finance_api',
                                    'get_finance_province_city_county')
    FINANCE_ALL_PROVINCE = ('cbbweb.service.page.finance.finance_api',
                            'get_finance_all_province')
    FINANCE_ALL_CITY = ('cbbweb.service.page.finance.finance_api',
                        'get_finance_all_city')
    FINANCE_ALL_COUNTY = ('cbbweb.service.page.finance.finance_api',
                          'get_finance_all_county')
    FINANCE_DEALER_PROVINCE = ('cbbweb.service.page.finance.finance_api',
                               'get_finance_dealer_province')
    FINANCE_DEALER_CITY = ('cbbweb.service.page.finance.finance_api',
                           'get_finance_dealer_city')
    FINANCE_DEALER_COUNTY = ('cbbweb.service.page.finance.finance_api',
                             'get_finance_dealer_county')

    # dep --- FINANCE_GROUP_BRAND_CAR_SERIES
    GROUP_BRAND_CAR_SERIES = ('cbbweb.service.page.finance.finance_api',
                              'get_group_brand_car_series')


    # COMMON #########################################
    PLACE_PROVINCE_BY_ID = ('cbbweb.service.page.common.common_api',
                            'get_place_province_by_id')

    PLACE_CITY_BY_ID = ('cbbweb.service.page.common.common_api',
                        'get_place_city_by_id')

    PLACE_COUNTY_BY_ID = ('cbbweb.service.page.common.common_api',
                          'get_place_county_by_id')

    # HOME #########################################

    # API BY PAGE END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    # ACTIVITY SERVICE START <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    CAR_SERIES_NEWEST_ACTIVITY = (DEALER_SERVICE,
                                  'get_car_series_newest_activity')
    CAR_SERIES_NEWEST_ACTIVITY_DICT = (DEALER_SERVICE,
                                       'get_car_series_newest_activity_dict')
    # ACTIVITY SERVICE END >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


    # CLUE_SERVICE START
    CLUE_SAVE_API = (CLUE_SERVICE, 'get_clue_save_api')
    # CLUE_SERVICE END

    # SMS_SERVICE START
    SEND_VERIFY_CODE = (SMS_SERVICE, 'send_verify_code')
    VERIFY_CODE = (SMS_SERVICE, 'verify_code')
    # SMS_SERVICE END



   
