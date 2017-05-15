# -*- coding: utf-8 -*-



def append_kwargs(model_name, kwargs):
    # append is_enable=1 is_show=1 is_frozen=0
    if model_name in APPEND_KWARGS_DICT:
        if not kwargs:
            kwargs = {}
        table_append_dict = APPEND_KWARGS_DICT[model_name]
        for append_key in table_append_dict:
            kwargs[append_key] = table_append_dict[append_key]
    return kwargs


APPEND_KWARGS_DICT = {
    'TBaseAdContent': {
        'is_enable': 1,
    },
    'TBaseAdPositionType': {
        'is_enable': 1,
    },
    'TBaseAdvertisement': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseBigarea': {
        'is_enable': 1,
    },
    'TBaseBrand': {
        'is_enable': 1,
    },
    'TBaseCarBrand': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCarBrandMdm': {
        'is_enable': 1,
    },
    'TBaseCarColor': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCarColorMdm': {
        'is_enable': 1,
    },
    'TBaseCarIncolorMdm': {
        'is_enable': 1,
    },
    'TBaseCarOwner': {
        'is_enable': 1,
    },
    'TBaseCarSeries': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCarSeriesMapping': {
        'is_enable': 1,
    },
    'TBaseCarSeriesMdm': {
        'is_enable': 1,
    },
    'TBaseCarType': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCarTypeMapping': {
        'is_enable': 1,
    },
    'TBaseCarTypeProperty': {
        'is_enable': 1,
    },
    'TBaseCarTypePropertyTemplate': {
        'is_enable': 1,
    },
    'TBaseCategory': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCity': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseCommonPraise': {
        'is_enable': 1,
    },
    'TBaseCommonPraiseReply': {
        'is_enable': 1,
    },
    'TBaseCounty': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseDataDict': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseDataDictGroup': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseDealer': {
        'is_enable': 1,
        'is_frozen': 0,
    },
    'TBaseDealerMapping': {
        'is_enable': 1,
    },
    'TBaseDealerMdm': {
        'is_enable': 1,
    },
    'TBaseEmployee': {
        'is_enable': 1,
    },
    'TBaseFinancialConditionRel': {
        'is_enable': 1,
    },
    'TBaseFinancialCorp': {
        'is_enable': 1,
    },
    'TBaseFinancialDlrRel': {
        'is_enable': 1,
    },
    'TBaseFinancialFeatureRel': {
        'is_enable': 1,
    },
    'TBaseFinancialFirstPayPercentRel': {
        'is_enable': 1,
    },
    'TBaseFinancialMaterialRel': {
        'is_enable': 1,
    },
    'TBaseFinancialProSku': {
        'is_enable': 1,
    },
    'TBaseFinancialProduct': {
        'is_enable': 1,
    },
    'TBaseFinancialSeriesRel': {
        'is_enable': 1,
    },
    'TBaseLargeCarType': {
        'is_enable': 1,
    },
    'TBaseMediaActivity': {
        'is_enable': 1,
    },
    'TBaseMediaActivity1': {
        'is_enable': 1,
    },
    'TBaseMediaActivityDealer': {
        'is_enable': 1,
    },
    'TBaseMediaActivityItems': {
        'is_enable': 1,
    },
    'TBaseMediaActivityType': {
        'is_enable': 1,
    },
    'TBaseMediaDealerActivity': {
        'is_enable': 1,
    },
    'TBaseMember': {
        'is_enable': 1,
    },
    'TBaseMemberContact': {
        'is_enable': 1,
    },
    'TBaseMemberExt': {
        'is_enable': 1,
    },
    'TBaseMemberFavorite': {
        'is_enable': 1,
    },
    'TBaseMemberStatus': {
        'is_enable': 1,
    },
    'TBaseMiddleCarType': {
        'is_enable': 1,
    },
    'TBaseOfferPrice': {
        'is_enable': 1,
    },
    'TBasePraiseScore': {
        'is_enable': 1,
    },
    'TBaseProduct': {
        'is_enable': 1,
    },
    'TBaseProductExt': {
        'is_enable': 1,
    },
    'TBaseProductImage': {
        'is_enable': 1,
    },
    'TBaseProductProperty': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseProductPropertyGroup': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseProductVideo': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBasePropertyGroupItem': {
        'is_enable': 1,
    },
    'TBasePropertyValue': {
        'is_enable': 1,
    },
    'TBaseProvince': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseRegion': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseSmallCarType': {
        'is_enable': 1,
    },
    'TBaseSmallarea': {
        'is_enable': 1,
    },
    'TBaseSystemInfo': {
        'is_enable': 1,
    },
    'TBaseSystemPubInfo': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TBaseTmallMember': {
        'is_enable': 1,
    },
    'TBaseWechatMember': {
        'is_enable': 1,
    },
    'TCmsCatalogs': {
        'is_enable': 1,
    },
    'TCmsCatatype': {
        'is_enable': 1,
    },
    'TCmsModels': {
        'is_enable': 1,
    },
    'TE4SDbRole': {
        'is_enable': 1,
    },
    'TE4SDbUserInfo': {
        'is_enable': 1,
    },
    'TEcommerceCardPayment': {
        'is_enable': 1,
    },
    'TEcommerceComment': {
        'is_enable': 1,
    },
    'TEcommerceCommodity': {
        'is_enable': 1,
    },
    'TEcommerceCommodityCarExt': {
        'is_enable': 1,
    },
    'TEcommerceCommodityDealer': {
        'is_enable': 1,
    },
    'TEcommerceCommodityExt': {
        'is_enable': 1,
    },
    'TEcommerceCommodityInventory': {
        'is_enable': 1,
    },
    'TEcommerceCommoditySku': {
        'is_enable': 1,
    },
    'TEcommerceCommodityVerifyExt': {
        'is_enable': 1,
    },
    'TEcommerceCoupon': {
        'is_enable': 1,
    },
    'TEcommerceCouponCard': {
        'is_enable': 1,
    },
    'TEcommerceCouponGroup': {
        'is_enable': 1,
    },
    'TEcommerceFinacialOrder': {
        'is_enable': 1,
    },
    'TEcommerceOrder': {
        'is_enable': 1,
    },
    'TEcommerceOrderAddress': {
        'is_enable': 1,
    },
    'TEcommerceOrderFlowstatus': {
        'is_enable': 1,
    },
    'TEcommerceOrderPayment': {
        'is_enable': 1,
    },
    'TEcommerceOrderShipment': {
        'is_enable': 1,
    },
    'TEcommerceOrderShipmentExt': {
        'is_enable': 1,
    },
    'TEcommerceOrderShipmentItem': {
        'is_enable': 1,
    },
    'TEcommerceOrderShipmentMessage': {
        'is_enable': 1,
    },
    'TEcommerceOrderSku': {
        'is_enable': 1,
    },
    'TEcommercePaymentgateway': {
        'is_show': 1,
        'is_enable': 1,
    },
    'TEcommercePaymentgatewayProperty': {
        'is_enable': 1,
    },
    'TEcommerceVerified': {
        'is_enable': 1,
    },
}

