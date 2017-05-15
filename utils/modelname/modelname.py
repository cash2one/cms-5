# -*- coding: utf-8 -*-

from enum import Enum

#from cbbweb.cms import models

class ModelName(Enum):
    T_BASE_AD_CONTENT = "TBaseAdContent"
    T_BASE_AD_POSITION_TYPE = "TBaseAdPositionType"
    T_BASE_ADVERTISEMENT = "TBaseAdvertisement"
    T_BASE_BIGAREA = "TBaseBigarea"
    T_BASE_BRAND = "TBaseBrand"
    T_BASE_CAR_BRAND = "TBaseCarBrand"
    T_BASE_CAR_BRAND_MDM = "TBaseCarBrandMdm"
    T_BASE_CAR_COLOR = "TBaseCarColor"
    T_BASE_CAR_COLOR_MDM = "TBaseCarColorMdm"
    T_BASE_CAR_INCOLOR_MDM = "TBaseCarIncolorMdm"
    T_BASE_CAR_OWNER = "TBaseCarOwner"
    T_BASE_CAR_SERIES = "TBaseCarSeries"
    T_BASE_CAR_SERIES_MAPPING = "TBaseCarSeriesMapping"
    T_BASE_CAR_SERIES_MDM = "TBaseCarSeriesMdm"
    T_BASE_CAR_TYPE = "TBaseCarType"
    T_BASE_CAR_TYPE_MAPPING = "TBaseCarTypeMapping"
    T_BASE_CAR_TYPE_PROPERTY = "TBaseCarTypeProperty"
    T_BASE_CAR_TYPE_PROPERTY_TEMPLATE = "TBaseCarTypePropertyTemplate"
    T_BASE_CATEGORY = "TBaseCategory"
    T_BASE_CITY = "TBaseCity"
    T_BASE_COMMON_PRAISE = "TBaseCommonPraise"
    T_BASE_COMMON_PRAISE_REPLY = "TBaseCommonPraiseReply"
    T_BASE_COUNTY = "TBaseCounty"
    T_BASE_DATA_DICT = "TBaseDataDict"
    T_BASE_DATA_DICT_GROUP = "TBaseDataDictGroup"
    T_BASE_DEALER = "TBaseDealer"
    T_BASE_DEALER_MAPPING = "TBaseDealerMapping"
    T_BASE_DEALER_MDM = "TBaseDealerMdm"
    T_BASE_EMPLOYEE = "TBaseEmployee"
    T_BASE_FINANCIAL_CONDITION_REL = "TBaseFinancialConditionRel"
    T_BASE_FINANCIAL_CORP = "TBaseFinancialCorp"
    T_BASE_FINANCIAL_DLR_REL = "TBaseFinancialDlrRel"
    T_BASE_FINANCIAL_FEATURE_REL = "TBaseFinancialFeatureRel"
    T_BASE_FINANCIAL_FIRST_PAY_PERCENT_REL = "TBaseFinancialFirstPayPercentRel"
    T_BASE_FINANCIAL_MATERIAL_REL = "TBaseFinancialMaterialRel"
    T_BASE_FINANCIAL_PRO_SKU = "TBaseFinancialProSku"
    T_BASE_FINANCIAL_PRODUCT = "TBaseFinancialProduct"
    T_BASE_FINANCIAL_SERIES_REL = "TBaseFinancialSeriesRel"
    T_BASE_LARGE_CAR_TYPE = "TBaseLargeCarType"
    T_BASE_MEDIA_ACTIVITY = "TBaseMediaActivity"
    T_BASE_MEDIA_ACTIVITY_TYPE = "TBaseMediaActivityType"
    T_BASE_MEMBER = "TBaseMember"
    T_BASE_MEMBER_CONTACT = "TBaseMemberContact"
    T_BASE_MEMBER_EXT = "TBaseMemberExt"
    T_BASE_MEMBER_FAVORITE = "TBaseMemberFavorite"
    T_BASE_MEMBER_STATUS = "TBaseMemberStatus"
    T_BASE_MIDDLE_CAR_TYPE = "TBaseMiddleCarType"
    T_BASE_OFFER_PRICE = "TBaseOfferPrice"
    T_BASE_PRAISE_SCORE = "TBasePraiseScore"
    T_BASE_PRODUCT = "TBaseProduct"
    T_BASE_PRODUCT_EXT = "TBaseProductExt"
    T_BASE_PRODUCT_IMAGE = "TBaseProductImage"
    T_BASE_PRODUCT_PROPERTY = "TBaseProductProperty"
    T_BASE_PRODUCT_PROPERTY_GROUP = "TBaseProductPropertyGroup"
    T_BASE_PRODUCT_VIDEO = "TBaseProductVideo"
    T_BASE_PROPERTY_GROUP_ITEM = "TBasePropertyGroupItem"
    T_BASE_PROPERTY_VALUE = "TBasePropertyValue"
    T_BASE_PROVINCE = "TBaseProvince"
    T_BASE_REGION = "TBaseRegion"
    T_BASE_SMALL_CAR_TYPE = "TBaseSmallCarType"
    T_BASE_SMALLAREA = "TBaseSmallarea"
    T_BASE_SYSTEM_INFO = "TBaseSystemInfo"
    T_BASE_SYSTEM_PUB_INFO = "TBaseSystemPubInfo"
    T_BASE_TMALL_MEMBER = "TBaseTmallMember"
    T_BASE_WECHAT_MEMBER = "TBaseWechatMember"
    T_CMS_ARTICLE = "TCmsArticle"
    T_CMS_ARTICLE_RELA = "TCmsArticleRela"
    T_CMS_CATA_ATTRS = "TCmsCataAttrs"
    T_CMS_CATALOGS = "TCmsCatalogs"
    T_CMS_CATATYPE = "TCmsCatatype"
    T_CMS_CATATYPE_ATTRS = "TCmsCatatypeAttrs"
    T_CMS_LINKWORD = "TCmsLinkword"
    T_CMS_MODELS = "TCmsModels"
    T_CMS_SECTION = "TCmsSection"
    T_CMS_TEMPLATE = "TCmsTemplate"
    T_E4S_DB_CUSTOMER_ACCOUNT = "TE4SDbCustomerAccount"
    T_E4S_DB_DICTIONARY_DATA = "TE4SDbDictionaryData"
    T_E4S_DB_DICTIONARY_TYPE = "TE4SDbDictionaryType"
    T_E4S_DB_FUNCTION = "TE4SDbFunction"
    T_E4S_DB_LOG_MESSAGE = "TE4SDbLogMessage"
    T_E4S_DB_LOG_REGISTER = "TE4SDbLogRegister"
    T_E4S_DB_PASSWORD_HISTORY = "TE4SDbPasswordHistory"
    T_E4S_DB_ROLE = "TE4SDbRole"
    T_E4S_DB_ROLE_FUNCTION = "TE4SDbRoleFunction"
    T_E4S_DB_USER = "TE4SDbUser"
    T_E4S_DB_USER_INFO = "TE4SDbUserInfo"
    T_E4S_DB_USER_ROLE = "TE4SDbUserRole"
    T_ECOMMERCE_CARD_PAYMENT = "TEcommerceCardPayment"
    T_ECOMMERCE_COMMENT = "TEcommerceComment"
    T_ECOMMERCE_COMMODITY = "TEcommerceCommodity"
    T_ECOMMERCE_COMMODITY_CAR_EXT = "TEcommerceCommodityCarExt"
    T_ECOMMERCE_COMMODITY_DEALER = "TEcommerceCommodityDealer"
    T_ECOMMERCE_COMMODITY_EXT = "TEcommerceCommodityExt"
    T_ECOMMERCE_COMMODITY_INVENTORY = "TEcommerceCommodityInventory"
    T_ECOMMERCE_COMMODITY_SKU = "TEcommerceCommoditySku"
    T_ECOMMERCE_COMMODITY_VERIFY_EXT = "TEcommerceCommodityVerifyExt"
    T_ECOMMERCE_COUPON = "TEcommerceCoupon"
    T_ECOMMERCE_COUPON_CARD = "TEcommerceCouponCard"
    T_ECOMMERCE_COUPON_GROUP = "TEcommerceCouponGroup"
    T_ECOMMERCE_FINACIAL_ORDER = "TEcommerceFinacialOrder"
    T_ECOMMERCE_ORDER = "TEcommerceOrder"
    T_ECOMMERCE_ORDER_ADDRESS = "TEcommerceOrderAddress"
    T_ECOMMERCE_ORDER_FLOWSTATUS = "TEcommerceOrderFlowstatus"
    T_ECOMMERCE_ORDER_PAYMENT = "TEcommerceOrderPayment"
    T_ECOMMERCE_ORDER_SHIPMENT = "TEcommerceOrderShipment"
    T_ECOMMERCE_ORDER_SHIPMENT_EXT = "TEcommerceOrderShipmentExt"
    T_ECOMMERCE_ORDER_SHIPMENT_ITEM = "TEcommerceOrderShipmentItem"
    T_ECOMMERCE_ORDER_SKU = "TEcommerceOrderSku"
    T_ECOMMERCE_PAYMENTGATEWAY = "TEcommercePaymentgateway"
    T_ECOMMERCE_PAYMENTGATEWAY_PROPERTY = "TEcommercePaymentgatewayProperty"
    T_ECOMMERCE_VERIFIED = "TEcommerceVerified"