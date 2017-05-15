# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class TBaseAdContent(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ad_content = models.TextField(db_column='AD_CONTENT', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_ad_content'


class TBaseAdPositionType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    position_name = models.CharField(db_column='POSITION_NAME', max_length=128)  # Field name made lowercase.
    position_code = models.CharField(db_column='POSITION_CODE', max_length=32)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    position_type = models.SmallIntegerField(db_column='POSITION_TYPE', blank=True, null=True)  # Field name made lowercase.
    display_type = models.SmallIntegerField(db_column='DISPLAY_TYPE', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_ad_position_type'


class TBaseAdvertisement(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    adpositiontype_id = models.IntegerField(db_column='ADPOSITIONTYPE_ID', blank=True, null=True)  # Field name made lowercase.
    advertisement_name = models.CharField(db_column='ADVERTISEMENT_NAME', max_length=128)  # Field name made lowercase.
    content_type = models.SmallIntegerField(db_column='CONTENT_TYPE')  # Field name made lowercase.
    advertisement_detail = models.CharField(db_column='ADVERTISEMENT_DETAIL', max_length=512, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255)  # Field name made lowercase.
    redirect_url = models.CharField(db_column='REDIRECT_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    width = models.DecimalField(db_column='WIDTH', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    height = models.DecimalField(db_column='HEIGHT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    start_publish_time = models.DateTimeField(db_column='START_PUBLISH_TIME', blank=True, null=True)  # Field name made lowercase.
    end_publish_time = models.DateTimeField(db_column='END_PUBLISH_TIME', blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO')  # Field name made lowercase.
    is_show = models.SmallIntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_advertisement'


class TBaseBigarea(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36)  # Field name made lowercase.
    big_area_name = models.CharField(db_column='BIG_AREA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    brand_code = models.CharField(db_column='BRAND_CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_bigarea'


class TBaseBrand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    brand_name_cn = models.CharField(db_column='BRAND_NAME_CN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand_name_en = models.CharField(db_column='BRAND_NAME_EN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand_code = models.CharField(db_column='BRAND_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brand_logo = models.CharField(db_column='BRAND_LOGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_brand'


class TBaseCarBrand(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_brand_en = models.CharField(db_column='CAR_BRAND_EN', max_length=50)  # Field name made lowercase.
    car_brand_cn = models.CharField(db_column='CAR_BRAND_CN', max_length=50)  # Field name made lowercase.
    car_brand_alias = models.CharField(db_column='CAR_BRAND_ALIAS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logo_img = models.CharField(db_column='LOGO_IMG', max_length=256, blank=True, null=True)  # Field name made lowercase.
    mdm_car_brand_code = models.CharField(db_column='MDM_CAR_BRAND_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mdm_car_brand_en = models.CharField(db_column='MDM_CAR_BRAND_EN', max_length=50)  # Field name made lowercase.
    mdm_car_brand_cn = models.CharField(db_column='MDM_CAR_BRAND_CN', max_length=50)  # Field name made lowercase.
    product_brand_id = models.IntegerField(db_column='PRODUCT_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_brand'


class TBaseCarBrandMdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    car_brand_en = models.CharField(db_column='CAR_BRAND_EN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_brand_cn = models.CharField(db_column='CAR_BRAND_CN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_brand_mdm'


class TBaseCarColor(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    color_type = models.IntegerField(db_column='COLOR_TYPE')  # Field name made lowercase.
    color_name = models.CharField(db_column='COLOR_NAME', max_length=50)  # Field name made lowercase.
    mdm_color_id = models.CharField(db_column='MDM_COLOR_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    rgb_value = models.CharField(db_column='RGB_VALUE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_color'


class TBaseCarColorMdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_color_id = models.CharField(db_column='CAR_COLOR_ID', max_length=36)  # Field name made lowercase.
    car_color_code = models.CharField(db_column='CAR_COLOR_CODE', max_length=50)  # Field name made lowercase.
    car_color_name = models.CharField(db_column='CAR_COLOR_NAME', max_length=100)  # Field name made lowercase.
    supply_status = models.CharField(db_column='SUPPLY_STATUS', max_length=2)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    color_bolid = models.CharField(db_column='COLOR_BOLID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_color_mdm'


class TBaseCarIncolorMdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_incolor_id = models.CharField(db_column='CAR_INCOLOR_ID', max_length=36)  # Field name made lowercase.
    car_incolor_code = models.CharField(db_column='CAR_INCOLOR_CODE', max_length=50)  # Field name made lowercase.
    car_incolor_name = models.CharField(db_column='CAR_INCOLOR_NAME', max_length=100)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    color_bolid = models.CharField(db_column='COLOR_BOLID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_incolor_mdm'


class TBaseCarOwner(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID')  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_code = models.CharField(db_column='CAR_SERIES_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    exterior_color = models.CharField(db_column='EXTERIOR_COLOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interior_color = models.CharField(db_column='INTERIOR_COLOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    ic_card_no = models.CharField(db_column='IC_CARD_NO', max_length=17, blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=20, blank=True, null=True)  # Field name made lowercase.
    car_no = models.CharField(db_column='CAR_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    engine_no = models.CharField(db_column='ENGINE_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    points = models.CharField(db_column='POINTS', max_length=128, blank=True, null=True)  # Field name made lowercase.
    card_degree_name = models.CharField(db_column='CARD_DEGREE_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    purchasing_date = models.DateField(db_column='PURCHASING_DATE', blank=True, null=True)  # Field name made lowercase.
    cust_no = models.CharField(db_column='CUST_NO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_parter = models.IntegerField(db_column='IS_PARTER', blank=True, null=True)  # Field name made lowercase.
    reg_parter_time = models.DateTimeField(db_column='REG_PARTER_TIME', blank=True, null=True)  # Field name made lowercase.
    ca = models.CharField(db_column='CA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sa = models.CharField(db_column='SA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_owner'


class TBaseCarSeries(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mdm_car_series_id = models.CharField(db_column='MDM_CAR_SERIES_ID', max_length=36)  # Field name made lowercase.
    mdm_car_series_code = models.CharField(db_column='MDM_CAR_SERIES_CODE', max_length=50)  # Field name made lowercase.
    car_brand_id = models.IntegerField(db_column='CAR_BRAND_ID')  # Field name made lowercase.
    car_series_cn = models.CharField(db_column='CAR_SERIES_CN', max_length=50)  # Field name made lowercase.
    car_series_en = models.CharField(db_column='CAR_SERIES_EN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_level = models.IntegerField(db_column='CAR_LEVEL', blank=True, null=True)  # Field name made lowercase.
    official_car_level = models.IntegerField(db_column='OFFICIAL_CAR_LEVEL', blank=True, null=True)  # Field name made lowercase.
    car_series_alias = models.CharField(db_column='CAR_SERIES_ALIAS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    car_property = models.CharField(db_column='CAR_PROPERTY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    pc_thumbnail = models.CharField(db_column='PC_THUMBNAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    multi_angle_img = models.CharField(db_column='MULTI_ANGLE_IMG', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    wap_thumbnail = models.CharField(db_column='WAP_THUMBNAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    brief_introdution = models.CharField(db_column='BRIEF_INTRODUTION', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    energy_category = models.IntegerField(db_column='ENERGY_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    start_guideprice = models.IntegerField(db_column='START_GUIDEPRICE', blank=True, null=True)  # Field name made lowercase.
    end_guideprice = models.IntegerField(db_column='END_GUIDEPRICE', blank=True, null=True)  # Field name made lowercase.
    is_testdrive = models.CharField(db_column='IS_TESTDRIVE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    structure = models.CharField(db_column='STRUCTURE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    sales = models.IntegerField(db_column='SALES', blank=True, null=True)  # Field name made lowercase.
    qczj_grade = models.CharField(db_column='QCZJ_GRADE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    ycw_grade = models.CharField(db_column='YCW_GRADE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    tpyqc_grade = models.CharField(db_column='TPYQC_GRADE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    akqc_grade = models.CharField(db_column='AKQC_GRADE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    order_no = models.DecimalField(db_column='ORDER_NO', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_series'


class TBaseCarSeriesMapping(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    media_car_series_id = models.CharField(db_column='MEDIA_CAR_SERIES_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_car_series_name = models.CharField(db_column='MEDIA_CAR_SERIES_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_from = models.CharField(db_column='MEDIA_FROM', max_length=64, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_series_mapping'


class TBaseCarSeriesMdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_series_id = models.CharField(db_column='CAR_SERIES_ID', max_length=36)  # Field name made lowercase.
    car_series_code = models.CharField(db_column='CAR_SERIES_CODE', max_length=50)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    car_series_cn = models.CharField(db_column='CAR_SERIES_CN', max_length=50)  # Field name made lowercase.
    car_series_en = models.CharField(db_column='CAR_SERIES_EN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    gdsname = models.CharField(db_column='GDSNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    begin_date = models.DateTimeField(db_column='BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    end_date = models.DateTimeField(db_column='END_DATE', blank=True, null=True)  # Field name made lowercase.
    part_series_code = models.CharField(db_column='PART_SERIES_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    answer_car_series_id = models.CharField(db_column='ANSWER_CAR_SERIES_ID', max_length=20, blank=True, null=True)  # Field name made lowercase.
    old_carseries_id = models.DecimalField(db_column='OLD_CARSERIES_ID', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    sap_carseries_code = models.CharField(db_column='SAP_CARSERIES_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_series_mdm'


class TBaseCarType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mdm_car_type_code = models.CharField(db_column='MDM_CAR_TYPE_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_brand_id = models.IntegerField(db_column='CAR_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    model_year = models.CharField(db_column='MODEL_YEAR', max_length=10, blank=True, null=True)  # Field name made lowercase.
    car_type_name = models.CharField(db_column='CAR_TYPE_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    car_level = models.IntegerField(db_column='CAR_LEVEL', blank=True, null=True)  # Field name made lowercase.
    guide_price = models.IntegerField(db_column='GUIDE_PRICE', blank=True, null=True)  # Field name made lowercase.
    offer_price_section = models.CharField(db_column='OFFER_PRICE_SECTION', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_type_status = models.IntegerField(db_column='CAR_TYPE_STATUS', blank=True, null=True)  # Field name made lowercase.
    color_code = models.CharField(db_column='COLOR_CODE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    incolor_code = models.CharField(db_column='INCOLOR_CODE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    quality_assurance = models.IntegerField(db_column='QUALITY_ASSURANCE', blank=True, null=True)  # Field name made lowercase.
    characteristic_activity = models.CharField(db_column='CHARACTERISTIC_ACTIVITY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    product_spot = models.CharField(db_column='PRODUCT_SPOT', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.
    e4s_car_type_id = models.CharField(db_column='E4S_CAR_TYPE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_type'


class TBaseCarTypeMapping(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_type_id = models.IntegerField(db_column='CAR_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    media_car_type_id = models.CharField(db_column='MEDIA_CAR_TYPE_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_car_type_name = models.CharField(db_column='MEDIA_CAR_TYPE_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_from = models.CharField(db_column='MEDIA_FROM', max_length=64, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_type_mapping'


class TBaseCarTypeProperty(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    car_type_id = models.IntegerField(db_column='CAR_TYPE_ID')  # Field name made lowercase.
    property_id = models.IntegerField(db_column='PROPERTY_ID')  # Field name made lowercase.
    property_value = models.CharField(db_column='PROPERTY_VALUE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE')  # Field name made lowercase.
    e4s_car_type_id = models.CharField(db_column='E4S_CAR_TYPE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_type_property'


class TBaseCarTypePropertyTemplate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    property_key = models.CharField(db_column='PROPERTY_KEY', max_length=50)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=32)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID')  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=128, blank=True, null=True)  # Field name made lowercase.
    is_editable = models.CharField(db_column='IS_EDITABLE', max_length=1)  # Field name made lowercase.
    defualt_value = models.CharField(db_column='DEFUALT_VALUE', max_length=256, blank=True, null=True)  # Field name made lowercase.
    edit_type = models.CharField(db_column='EDIT_TYPE', max_length=2, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    update_date = models.DateTimeField(db_column='UPDATE_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_car_type_property_template'


class TBaseCategory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    category_name = models.CharField(db_column='CATEGORY_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    category_type = models.IntegerField(db_column='CATEGORY_TYPE', blank=True, null=True)  # Field name made lowercase.
    category_level = models.IntegerField(db_column='CATEGORY_LEVEL', blank=True, null=True)  # Field name made lowercase.
    category_desc = models.CharField(db_column='CATEGORY_DESC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    used_by_dlr = models.CharField(db_column='USED_BY_DLR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    tree_path = models.CharField(db_column='TREE_PATH', max_length=32, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_category'


class TBaseCity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36)  # Field name made lowercase.
    city_code = models.CharField(db_column='CITY_CODE', max_length=50)  # Field name made lowercase.
    city_name = models.CharField(db_column='CITY_NAME', max_length=100)  # Field name made lowercase.
    city_alias = models.CharField(db_column='CITY_ALIAS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    is_limited = models.CharField(db_column='IS_LIMITED', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_capital = models.CharField(db_column='IS_CAPITAL', max_length=2)  # Field name made lowercase.
    is_popular = models.CharField(db_column='IS_POPULAR', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_municipality = models.CharField(db_column='IS_MUNICIPALITY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    regionalism_code = models.CharField(db_column='REGIONALISM_CODE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=32)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=32)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_city'


class TBaseCommonPraise(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    common_praise_type = models.IntegerField(db_column='COMMON_PRAISE_TYPE', blank=True, null=True)  # Field name made lowercase.
    target_id = models.IntegerField(db_column='TARGET_ID', blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    owner_id = models.IntegerField(db_column='OWNER_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pub_date = models.CharField(db_column='PUB_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pictures = models.CharField(db_column='PICTURES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visit = models.IntegerField(db_column='VISIT', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    scores = models.TextField(db_column='SCORES', blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_common_praise'


class TBaseCommonPraiseReply(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    common_praise_id = models.IntegerField(db_column='COMMON_PRAISE_ID', blank=True, null=True)  # Field name made lowercase.
    ref_id = models.IntegerField(db_column='REF_ID', blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    common_praise_type = models.IntegerField(db_column='COMMON_PRAISE_TYPE', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pub_date = models.CharField(db_column='PUB_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pictures = models.CharField(db_column='PICTURES', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    visit = models.IntegerField(db_column='VISIT', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_common_praise_reply'


class TBaseCounty(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36)  # Field name made lowercase.
    county_code = models.CharField(db_column='COUNTY_CODE', max_length=50)  # Field name made lowercase.
    county_name = models.CharField(db_column='COUNTY_NAME', max_length=100)  # Field name made lowercase.
    regionalism_code = models.CharField(db_column='REGIONALISM_CODE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=32)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=32)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_county'


class TBaseDataDict(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dictgroup_id = models.IntegerField(db_column='DICTGROUP_ID', blank=True, null=True)  # Field name made lowercase.
    dict_key = models.CharField(db_column='DICT_KEY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dict_value = models.CharField(db_column='DICT_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dict_ext_values = models.CharField(db_column='DICT_EXT_VALUES', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_data_dict'


class TBaseDataDictGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dictgroup_name = models.CharField(db_column='DICTGROUP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_data_dict_group'


class TBaseDealer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=10)  # Field name made lowercase.
    dlr_short_name = models.CharField(db_column='DLR_SHORT_NAME', max_length=50)  # Field name made lowercase.
    dlr_full_name = models.CharField(db_column='DLR_FULL_NAME', max_length=200)  # Field name made lowercase.
    dlr_prop = models.CharField(db_column='DLR_PROP', max_length=36, blank=True, null=True)  # Field name made lowercase.
    parent_dlr_id = models.CharField(db_column='PARENT_DLR_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dlr_status = models.CharField(db_column='DLR_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_level = models.CharField(db_column='DLR_LEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    car_series_ids = models.CharField(db_column='CAR_SERIES_IDS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    sale_city_ids = models.CharField(db_column='SALE_CITY_IDS', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    group_id = models.CharField(db_column='GROUP_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sale_tel = models.CharField(db_column='SALE_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_tel = models.CharField(db_column='SERVICE_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_tel_sub = models.CharField(db_column='SERVICE_TEL_SUB', max_length=200, blank=True, null=True)  # Field name made lowercase.
    insurance_tel = models.CharField(db_column='INSURANCE_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    urg_sos_tel = models.CharField(db_column='URG_SOS_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mdm_car_brand_code = models.CharField(db_column='MDM_CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    cbb_car_brand_code = models.CharField(db_column='CBB_CAR_BRAND_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    business_domain = models.CharField(db_column='BUSINESS_DOMAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    subdivision_business = models.CharField(db_column='SUBDIVISION_BUSINESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_vip = models.IntegerField(db_column='IS_VIP', blank=True, null=True)  # Field name made lowercase.
    service_auth = models.CharField(db_column='SERVICE_AUTH', max_length=500, blank=True, null=True)  # Field name made lowercase.
    pre_sales_score = models.DecimalField(db_column='PRE_SALES_SCORE', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    after_sales_score = models.DecimalField(db_column='AFTER_SALES_SCORE', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    pre_sales_score_prop = models.DecimalField(db_column='PRE_SALES_SCORE_PROP', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    after_sales_score_prop = models.DecimalField(db_column='AFTER_SALES_SCORE_PROP', max_digits=8, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    clue_handle_efficiency = models.CharField(db_column='CLUE_HANDLE_EFFICIENCY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    dlr_liveness = models.CharField(db_column='DLR_LIVENESS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_frozen = models.IntegerField(db_column='IS_FROZEN', blank=True, null=True)  # Field name made lowercase.
    freeze_reason = models.CharField(db_column='FREEZE_REASON', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dlr_image_url = models.CharField(db_column='DLR_IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    cont_address = models.CharField(db_column='CONT_ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    zip_code = models.CharField(db_column='ZIP_CODE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    longitude = models.DecimalField(db_column='LONGITUDE', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    latitude = models.DecimalField(db_column='LATITUDE', max_digits=10, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    alipay_no = models.CharField(db_column='ALIPAY_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alipay_name = models.CharField(db_column='ALIPAY_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    alipay_key = models.CharField(db_column='ALIPAY_KEY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_no = models.CharField(db_column='WECHAT_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_app_id = models.CharField(db_column='WECHAT_APP_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_app_secret = models.CharField(db_column='WECHAT_APP_SECRET', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_poi_id = models.CharField(db_column='WECHAT_POI_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    wechat_encoding_aes_key = models.CharField(db_column='WECHAT_ENCODING_AES_KEY', max_length=64, blank=True, null=True)  # Field name made lowercase.
    wechat_token = models.CharField(db_column='WECHAT_TOKEN', max_length=32, blank=True, null=True)  # Field name made lowercase.
    account_name = models.CharField(db_column='ACCOUNT_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    opening_bank = models.CharField(db_column='OPENING_BANK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    opening_account = models.CharField(db_column='OPENING_ACCOUNT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_dlr_num = models.CharField(db_column='WECHAT_DLR_NUM', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_sync_wechat = models.IntegerField(db_column='IS_SYNC_WECHAT', blank=True, null=True)  # Field name made lowercase.
    is_sync_mdm = models.IntegerField(db_column='IS_SYNC_MDM', blank=True, null=True)  # Field name made lowercase.
    is_sync_offer_price = models.IntegerField(db_column='IS_SYNC_OFFER_PRICE', blank=True, null=True)  # Field name made lowercase.
    is_agreement = models.IntegerField(db_column='IS_AGREEMENT', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_dealer'


class TBaseDealerMapping(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    media_dealer_id = models.CharField(db_column='MEDIA_DEALER_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_dealer_name = models.CharField(db_column='MEDIA_DEALER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    media_from = models.CharField(db_column='MEDIA_FROM', max_length=64, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_dealer_mapping'


class TBaseDealerMdm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    mdm_dlr_id = models.CharField(db_column='MDM_DLR_ID', max_length=36)  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=10)  # Field name made lowercase.
    dlr_short_name = models.CharField(db_column='DLR_SHORT_NAME', max_length=100)  # Field name made lowercase.
    dlr_full_name = models.CharField(db_column='DLR_FULL_NAME', max_length=200)  # Field name made lowercase.
    dlr_en_name = models.CharField(db_column='DLR_EN_NAME', max_length=200, blank=True, null=True)  # Field name made lowercase.
    dlr_name_old = models.CharField(db_column='DLR_NAME_OLD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    company_name_old = models.CharField(db_column='COMPANY_NAME_OLD', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comp_spell = models.CharField(db_column='COMP_SPELL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    comp_type = models.CharField(db_column='COMP_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parent_dlr_id = models.CharField(db_column='PARENT_DLR_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dlr_answer_code = models.CharField(db_column='DLR_ANSWER_CODE', max_length=4, blank=True, null=True)  # Field name made lowercase.
    sap_dlr_id = models.CharField(db_column='SAP_DLR_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_symbol = models.CharField(db_column='DLR_SYMBOL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    guno = models.CharField(db_column='GUNO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    register_money = models.DecimalField(db_column='REGISTER_MONEY', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    s_register_money = models.DecimalField(db_column='S_REGISTER_MONEY', max_digits=18, decimal_places=6, blank=True, null=True)  # Field name made lowercase.
    dlr_hardware_class = models.CharField(db_column='DLR_HARDWARE_CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    show_acreage = models.CharField(db_column='SHOW_ACREAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    factory_acreage = models.CharField(db_column='FACTORY_ACREAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    cover_acreage = models.CharField(db_column='COVER_ACREAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tatol_acreage = models.CharField(db_column='TATOL_ACREAGE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    fare_range = models.CharField(db_column='FARE_RANGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    dlr_buss_date = models.DateTimeField(db_column='DLR_BUSS_DATE', blank=True, null=True)  # Field name made lowercase.
    dlr_level = models.CharField(db_column='DLR_LEVEL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_debut_time = models.DateTimeField(db_column='DLR_DEBUT_TIME', blank=True, null=True)  # Field name made lowercase.
    link_addr = models.CharField(db_column='LINK_ADDR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(db_column='PHONE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    urg_sos_tel = models.CharField(db_column='URG_SOS_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    tel_sale = models.CharField(db_column='TEL_SALE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sale_fax = models.CharField(db_column='SALE_FAX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    sale_email = models.CharField(db_column='SALE_EMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_tel_fix = models.CharField(db_column='SERVICE_TEL_FIX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_fax = models.CharField(db_column='SERVICE_FAX', max_length=200, blank=True, null=True)  # Field name made lowercase.
    service_email = models.CharField(db_column='SERVICE_EMAIL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    legal_person = models.CharField(db_column='LEGAL_PERSON', max_length=100, blank=True, null=True)  # Field name made lowercase.
    master_card = models.CharField(db_column='MASTER_CARD', max_length=20, blank=True, null=True)  # Field name made lowercase.
    master_card_type = models.CharField(db_column='MASTER_CARD_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    s_master = models.CharField(db_column='S_MASTER', max_length=100, blank=True, null=True)  # Field name made lowercase.
    s_master_conn = models.CharField(db_column='S_MASTER_CONN', max_length=200, blank=True, null=True)  # Field name made lowercase.
    s_addr = models.CharField(db_column='S_ADDR', max_length=400, blank=True, null=True)  # Field name made lowercase.
    manager_name = models.CharField(db_column='MANAGER_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    manager_tel = models.CharField(db_column='MANAGER_TEL', max_length=200, blank=True, null=True)  # Field name made lowercase.
    balance_certificate = models.CharField(db_column='BALANCE_CERTIFICATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    balance_date = models.DateTimeField(db_column='BALANCE_DATE', blank=True, null=True)  # Field name made lowercase.
    maintain_certificate = models.CharField(db_column='MAINTAIN_CERTIFICATE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    maintain_cert_date = models.DateTimeField(db_column='MAINTAIN_CERT_DATE', blank=True, null=True)  # Field name made lowercase.
    init_date = models.DateTimeField(db_column='INIT_DATE', blank=True, null=True)  # Field name made lowercase.
    group_id = models.CharField(db_column='GROUP_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    ceo = models.CharField(db_column='CEO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    ceo_conn = models.CharField(db_column='CEO_CONN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    org_model_code = models.CharField(db_column='ORG_MODEL_CODE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    init_flag = models.CharField(db_column='INIT_FLAG', max_length=26, blank=True, null=True)  # Field name made lowercase.
    certificate_flag = models.CharField(db_column='CERTIFICATE_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_status = models.CharField(db_column='DLR_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_releation = models.CharField(db_column='DLR_RELEATION', max_length=4, blank=True, null=True)  # Field name made lowercase.
    dlr_type = models.CharField(db_column='DLR_TYPE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    releation_status = models.CharField(db_column='RELEATION_STATUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=26, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=500, blank=True, null=True)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    doqd_flag = models.CharField(db_column='DOQD_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dlr_sort = models.CharField(db_column='DLR_SORT', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dp_org_id = models.CharField(db_column='DP_ORG_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    mds_big_area_id = models.CharField(db_column='MDS_BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    pv_comp_code = models.CharField(db_column='PV_COMP_CODE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    is_synchronous = models.CharField(db_column='IS_SYNCHRONOUS', max_length=10, blank=True, null=True)  # Field name made lowercase.
    area = models.CharField(db_column='AREA', max_length=36, blank=True, null=True)  # Field name made lowercase.
    org_type = models.CharField(db_column='ORG_TYPE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    link_dlr_id = models.CharField(db_column='LINK_DLR_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    online_flag = models.CharField(db_column='ONLINE_FLAG', max_length=10, blank=True, null=True)  # Field name made lowercase.
    online_time = models.DateTimeField(db_column='ONLINE_TIME', blank=True, null=True)  # Field name made lowercase.
    is_used_mds = models.CharField(db_column='IS_USED_MDS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_used_coc = models.CharField(db_column='IS_USED_COC', max_length=2, blank=True, null=True)  # Field name made lowercase.
    longitude = models.CharField(max_length=50, blank=True, null=True)
    latitude = models.CharField(max_length=50, blank=True, null=True)
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_dealer_mdm'


class TBaseEmployee(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    emp_id = models.CharField(db_column='EMP_ID', max_length=36)  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=10)  # Field name made lowercase.
    emp_code = models.CharField(db_column='EMP_CODE', max_length=10)  # Field name made lowercase.
    emp_name = models.CharField(db_column='EMP_NAME', max_length=100)  # Field name made lowercase.
    emp_status = models.CharField(db_column='EMP_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    emp_type = models.CharField(db_column='EMP_TYPE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sales_car_brand_id = models.IntegerField(db_column='SALES_CAR_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    wechat_qrcode = models.CharField(db_column='WECHAT_QRCODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=50, blank=True, null=True)  # Field name made lowercase.
    service_area = models.CharField(db_column='SERVICE_AREA', max_length=50, blank=True, null=True)  # Field name made lowercase.
    birth_date = models.DateTimeField(db_column='BIRTH_DATE', blank=True, null=True)  # Field name made lowercase.
    work_tel = models.CharField(db_column='WORK_TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=200, blank=True, null=True)  # Field name made lowercase.
    gender_code = models.CharField(db_column='GENDER_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    degree_code = models.CharField(db_column='DEGREE_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    person_addr = models.CharField(db_column='PERSON_ADDR', max_length=250, blank=True, null=True)  # Field name made lowercase.
    zip = models.CharField(db_column='ZIP', max_length=100, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='FAX', max_length=20, blank=True, null=True)  # Field name made lowercase.
    nationality_code = models.CharField(db_column='NATIONALITY_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    marriaged_code = models.CharField(db_column='MARRIAGED_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    native_place = models.CharField(db_column='NATIVE_PLACE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    school = models.CharField(db_column='SCHOOL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    degreepro = models.CharField(db_column='DEGREEPRO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    skill_special = models.CharField(db_column='SKILL_SPECIAL', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    family_phone = models.CharField(db_column='FAMILY_PHONE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    second_man = models.CharField(db_column='SECOND_MAN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    second_man_tel = models.CharField(db_column='SECOND_MAN_TEL', max_length=50, blank=True, null=True)  # Field name made lowercase.
    driver_date = models.DateTimeField(db_column='DRIVER_DATE', blank=True, null=True)  # Field name made lowercase.
    nation_code = models.CharField(db_column='NATION_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    business_date = models.DateTimeField(db_column='BUSINESS_DATE', blank=True, null=True)  # Field name made lowercase.
    employ_date = models.DateTimeField(db_column='EMPLOY_DATE', blank=True, null=True)  # Field name made lowercase.
    is_driver = models.CharField(db_column='IS_DRIVER', max_length=2, blank=True, null=True)  # Field name made lowercase.
    employ_type = models.CharField(db_column='EMPLOY_TYPE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    politics_code = models.CharField(db_column='POLITICS_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cred_type_code = models.CharField(db_column='CRED_TYPE_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    cred_no = models.CharField(db_column='CRED_NO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emp_class = models.CharField(db_column='EMP_CLASS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_pic = models.CharField(db_column='EMP_PIC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    self_estimate = models.CharField(db_column='SELF_ESTIMATE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dlr_id = models.CharField(db_column='DLR_ID', max_length=36)  # Field name made lowercase.
    station_id = models.CharField(db_column='STATION_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    head_manager = models.CharField(db_column='HEAD_MANAGER', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sec_dlr_id = models.CharField(db_column='SEC_DLR_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    sec_dlr_code = models.CharField(db_column='SEC_DLR_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    dept_id = models.CharField(db_column='DEPT_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_employee'


class TBaseFinancialConditionRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    condition_name = models.CharField(db_column='CONDITION_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    condition_id = models.IntegerField(db_column='CONDITION_ID')  # Field name made lowercase.
    finacial_product_id = models.IntegerField(db_column='FINACIAL_PRODUCT_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_condition_rel'


class TBaseFinancialCorp(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    corp_name = models.CharField(db_column='CORP_NAME', max_length=36, blank=True, null=True)  # Field name made lowercase.
    loan_hour = models.IntegerField(db_column='LOAN_HOUR', blank=True, null=True)  # Field name made lowercase.
    is_online_audit = models.CharField(db_column='IS_ONLINE_AUDIT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    corp_logo = models.CharField(db_column='CORP_LOGO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    success_num = models.IntegerField(db_column='SUCCESS_NUM', blank=True, null=True)  # Field name made lowercase.
    online_audit_link = models.CharField(db_column='ONLINE_AUDIT_LINK', max_length=200, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_corp'


class TBaseFinancialDlrRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    financial_product_id = models.IntegerField(db_column='FINANCIAL_PRODUCT_ID')  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    type_id = models.BigIntegerField(db_column='TYPE_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_dlr_rel'


class TBaseFinancialFeatureRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    feature_name = models.CharField(db_column='FEATURE_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    feature_id = models.IntegerField(db_column='FEATURE_ID')  # Field name made lowercase.
    finacial_product_id = models.IntegerField(db_column='FINACIAL_PRODUCT_ID')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_feature_rel'


class TBaseFinancialFirstPayPercentRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    first_pay_percent = models.CharField(db_column='FIRST_PAY_PERCENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    finacial_product_id = models.IntegerField(db_column='FINACIAL_PRODUCT_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_first_pay_percent_rel'


class TBaseFinancialMaterialRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='MATERIAL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    material_id = models.IntegerField(db_column='MATERIAL_ID')  # Field name made lowercase.
    finacial_product_id = models.IntegerField(db_column='FINACIAL_PRODUCT_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_material_rel'


class TBaseFinancialProSku(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sku_name = models.CharField(db_column='SKU_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    sku_item = models.IntegerField(db_column='SKU_ITEM', blank=True, null=True)  # Field name made lowercase.
    sku_rate = models.CharField(db_column='SKU_RATE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    finacial_product_id = models.IntegerField(db_column='FINACIAL_PRODUCT_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_pro_sku'


class TBaseFinancialProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    financial_product_name = models.CharField(db_column='FINANCIAL_PRODUCT_NAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    financial_corp_id = models.IntegerField(db_column='FINANCIAL_CORP_ID', blank=True, null=True)  # Field name made lowercase.
    pass_percent = models.IntegerField(db_column='PASS_PERCENT', blank=True, null=True)  # Field name made lowercase.
    effect_start_date = models.DateTimeField(db_column='EFFECT_START_DATE', blank=True, null=True)  # Field name made lowercase.
    effect_end_date = models.DateTimeField(db_column='EFFECT_END_DATE', blank=True, null=True)  # Field name made lowercase.
    repayment_type = models.CharField(db_column='REPAYMENT_TYPE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    computing_formula = models.CharField(db_column='COMPUTING_FORMULA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    is_final_payment = models.IntegerField(db_column='IS_FINAL_PAYMENT', blank=True, null=True)  # Field name made lowercase.
    final_payment_scale = models.CharField(db_column='FINAL_PAYMENT_SCALE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    contains_interest = models.IntegerField(db_column='CONTAINS_INTEREST', blank=True, null=True)  # Field name made lowercase.
    brand_ids = models.CharField(db_column='BRAND_IDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    region_ids = models.CharField(db_column='REGION_IDS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    province_ids = models.CharField(db_column='PROVINCE_IDS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    dealer_type = models.CharField(db_column='DEALER_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_activation = models.CharField(db_column='IS_ACTIVATION', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_product'


class TBaseFinancialSeriesRel(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    financial_product_id = models.IntegerField(db_column='FINANCIAL_PRODUCT_ID')  # Field name made lowercase.
    car_series_id = models.CharField(db_column='CAR_SERIES_ID', max_length=36)  # Field name made lowercase.
    type_id = models.BigIntegerField(db_column='TYPE_ID')  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_financial_series_rel'


class TBaseLargeCarType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    large_car_type_id = models.CharField(db_column='LARGE_CAR_TYPE_ID', max_length=36)  # Field name made lowercase.
    base_series_id = models.CharField(db_column='BASE_SERIES_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    large_car_type_code = models.CharField(db_column='LARGE_CAR_TYPE_CODE', max_length=50)  # Field name made lowercase.
    large_car_type_cn = models.CharField(db_column='LARGE_CAR_TYPE_CN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    large_car_type_en = models.CharField(db_column='LARGE_CAR_TYPE_EN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    car_series_code = models.CharField(db_column='CAR_SERIES_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_large_car_type'


class TBaseMediaActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_title = models.CharField(db_column='ACTIVITY_TITLE', max_length=255)  # Field name made lowercase.
    page_url = models.CharField(db_column='PAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activity_content = models.CharField(db_column='ACTIVITY_CONTENT', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    activity_begin_date = models.DateTimeField(db_column='ACTIVITY_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_end_date = models.DateTimeField(db_column='ACTIVITY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.CharField(db_column='ACTIVITY_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID')  # Field name made lowercase.
    car_type_id = models.IntegerField(db_column='CAR_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_brand_id = models.IntegerField(db_column='CAR_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_activity'


class TBaseMediaActivity1(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_title = models.CharField(db_column='ACTIVITY_TITLE', max_length=255)  # Field name made lowercase.
    page_url = models.CharField(db_column='PAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activity_content = models.CharField(db_column='ACTIVITY_CONTENT', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    activity_begin_date = models.DateTimeField(db_column='ACTIVITY_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_end_date = models.DateTimeField(db_column='ACTIVITY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.CharField(db_column='ACTIVITY_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activity_category = models.IntegerField(db_column='ACTIVITY_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    register_begin_date = models.DateTimeField(db_column='REGISTER_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    register_end_date = models.DateTimeField(db_column='REGISTER_END_DATE', blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    main_image = models.CharField(db_column='MAIN_IMAGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=128, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    audit_status = models.SmallIntegerField(db_column='AUDIT_STATUS', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_activity_1'


class TBaseMediaActivityDealer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_id = models.IntegerField(db_column='ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.IntegerField(db_column='BIG_AREA_ID', blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.IntegerField(db_column='SMALL_AREA_ID', blank=True, null=True)  # Field name made lowercase.
    province_id = models.IntegerField(db_column='PROVINCE_ID', blank=True, null=True)  # Field name made lowercase.
    city_id = models.IntegerField(db_column='CITY_ID', blank=True, null=True)  # Field name made lowercase.
    county_id = models.IntegerField(db_column='COUNTY_ID', blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_activity_dealer'


class TBaseMediaActivityItems(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_id = models.IntegerField(db_column='ACTIVITY_ID', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.SmallIntegerField(db_column='ACTIVITY_TYPE', blank=True, null=True)  # Field name made lowercase.
    car_type_id = models.IntegerField(db_column='CAR_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_brand_id = models.IntegerField(db_column='CAR_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    brand_id = models.IntegerField(db_column='BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    promotion_price = models.IntegerField(db_column='PROMOTION_PRICE', blank=True, null=True)  # Field name made lowercase.
    inventory_category = models.SmallIntegerField(db_column='INVENTORY_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_activity_items'


class TBaseMediaActivityType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_type = models.CharField(db_column='ACTIVITY_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=255)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_activity_type'


class TBaseMediaDealerActivity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    activity_title = models.CharField(db_column='ACTIVITY_TITLE', max_length=255)  # Field name made lowercase.
    page_url = models.CharField(db_column='PAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activity_content = models.CharField(db_column='ACTIVITY_CONTENT', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    activity_begin_date = models.DateTimeField(db_column='ACTIVITY_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_end_date = models.DateTimeField(db_column='ACTIVITY_END_DATE', blank=True, null=True)  # Field name made lowercase.
    activity_type = models.CharField(db_column='ACTIVITY_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    activity_category = models.IntegerField(db_column='ACTIVITY_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    register_begin_date = models.DateTimeField(db_column='REGISTER_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    register_end_date = models.DateTimeField(db_column='REGISTER_END_DATE', blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    main_image = models.CharField(db_column='MAIN_IMAGE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='LOCATION', max_length=128, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=500, blank=True, null=True)  # Field name made lowercase.
    priority = models.IntegerField(db_column='PRIORITY', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    audit_status = models.SmallIntegerField(db_column='AUDIT_STATUS', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_media_dealer_activity'


class TBaseMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    account_id = models.IntegerField(db_column='ACCOUNT_ID', blank=True, null=True)  # Field name made lowercase.
    member_category = models.IntegerField(db_column='MEMBER_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    member_code = models.CharField(db_column='MEMBER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='USERNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    real_name = models.CharField(db_column='REAL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    nick_name = models.CharField(db_column='NICK_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    gender = models.IntegerField(db_column='GENDER', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='AGE', blank=True, null=True)  # Field name made lowercase.
    birthday = models.DateField(db_column='BIRTHDAY', blank=True, null=True)  # Field name made lowercase.
    id_card = models.CharField(db_column='ID_CARD', max_length=64, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reg_date = models.DateTimeField(db_column='REG_DATE', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_member'


class TBaseMemberContact(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID')  # Field name made lowercase.
    showname = models.CharField(db_column='SHOWNAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    telephone = models.CharField(db_column='TELEPHONE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(db_column='MOBILE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_member_contact'


class TBaseMemberExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID')  # Field name made lowercase.
    customer_apply_status = models.IntegerField(db_column='CUSTOMER_APPLY_STATUS', blank=True, null=True)  # Field name made lowercase.
    apply_static = models.IntegerField(db_column='APPLY_STATIC', blank=True, null=True)  # Field name made lowercase.
    company = models.CharField(db_column='COMPANY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    earn = models.CharField(db_column='EARN', max_length=255, blank=True, null=True)  # Field name made lowercase.
    credit = models.CharField(db_column='CREDIT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    social_insurance = models.CharField(db_column='SOCIAL_INSURANCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cpf = models.CharField(db_column='CPF', max_length=255, blank=True, null=True)  # Field name made lowercase.
    living_status = models.CharField(db_column='LIVING_STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    county_id = models.IntegerField(db_column='COUNTY_ID', blank=True, null=True)  # Field name made lowercase.
    city_id = models.IntegerField(db_column='CITY_ID', blank=True, null=True)  # Field name made lowercase.
    province_id = models.IntegerField(db_column='PROVINCE_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_member_ext'


class TBaseMemberFavorite(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    payment_id = models.IntegerField(db_column='PAYMENT_ID', blank=True, null=True)  # Field name made lowercase.
    buy_period = models.IntegerField(db_column='BUY_PERIOD', blank=True, null=True)  # Field name made lowercase.
    need_experience = models.IntegerField(db_column='NEED_EXPERIENCE', blank=True, null=True)  # Field name made lowercase.
    psychological_price = models.IntegerField(db_column='PSYCHOLOGICAL_PRICE', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_member_favorite'


class TBaseMemberStatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    member_status = models.IntegerField(db_column='MEMBER_STATUS', blank=True, null=True)  # Field name made lowercase.
    active_begin_date = models.DateTimeField(db_column='ACTIVE_BEGIN_DATE', blank=True, null=True)  # Field name made lowercase.
    active_end_date = models.DateTimeField(db_column='ACTIVE_END_DATE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_member_status'


class TBaseMiddleCarType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    std_car_id = models.CharField(db_column='STD_CAR_ID', max_length=36)  # Field name made lowercase.
    large_car_type_id = models.CharField(db_column='LARGE_CAR_TYPE_ID', max_length=36)  # Field name made lowercase.
    std_car_code = models.CharField(db_column='STD_CAR_CODE', max_length=50)  # Field name made lowercase.
    std_car_cn = models.CharField(db_column='STD_CAR_CN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    std_car_en = models.CharField(db_column='STD_CAR_EN', max_length=100)  # Field name made lowercase.
    std_car_type_desc = models.CharField(db_column='STD_CAR_TYPE_DESC', max_length=200, blank=True, null=True)  # Field name made lowercase.
    special_flag = models.CharField(db_column='SPECIAL_FLAG', max_length=50, blank=True, null=True)  # Field name made lowercase.
    old_cartype_id = models.DecimalField(db_column='OLD_CARTYPE_ID', max_digits=20, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_middle_car_type'


class TBaseOfferPrice(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    car_type_id = models.IntegerField(db_column='CAR_TYPE_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_brand_id = models.IntegerField(db_column='CAR_BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    original_offer_price = models.IntegerField(db_column='ORIGINAL_OFFER_PRICE', blank=True, null=True)  # Field name made lowercase.
    public_offer_price = models.IntegerField(db_column='PUBLIC_OFFER_PRICE', blank=True, null=True)  # Field name made lowercase.
    car_type_status = models.IntegerField(db_column='CAR_TYPE_STATUS', blank=True, null=True)  # Field name made lowercase.
    inventory_category = models.SmallIntegerField(db_column='INVENTORY_CATEGORY', blank=True, null=True)  # Field name made lowercase.
    purchase_tax = models.CharField(db_column='PURCHASE_TAX', max_length=32, blank=True, null=True)  # Field name made lowercase.
    comercial_insurance = models.CharField(db_column='COMERCIAL_INSURANCE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    compulsory_insurance = models.CharField(db_column='COMPULSORY_INSURANCE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    insurance_off = models.CharField(db_column='INSURANCE_OFF', max_length=32, blank=True, null=True)  # Field name made lowercase.
    travel_tax = models.CharField(db_column='TRAVEL_TAX', max_length=32, blank=True, null=True)  # Field name made lowercase.
    lisence_cost = models.CharField(db_column='LISENCE_COST', max_length=32, blank=True, null=True)  # Field name made lowercase.
    other_cost = models.CharField(db_column='OTHER_COST', max_length=32, blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    city_id = models.CharField(db_column='CITY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    county_id = models.CharField(db_column='COUNTY_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.
    e4s_car_type_id = models.CharField(db_column='E4S_CAR_TYPE_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    e4s_dlr_code = models.CharField(db_column='E4S_DLR_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_offer_price'


class TBasePraiseScore(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    praise_id = models.IntegerField(db_column='PRAISE_ID')  # Field name made lowercase.
    score_key = models.CharField(db_column='SCORE_KEY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score_value = models.CharField(db_column='SCORE_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    score_type = models.IntegerField(db_column='SCORE_TYPE', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_praise_score'


class TBaseProduct(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    brand_id = models.IntegerField(db_column='BRAND_ID', blank=True, null=True)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    product_stat_id = models.IntegerField(db_column='PRODUCT_STAT_ID', blank=True, null=True)  # Field name made lowercase.
    default_product_sku_id = models.IntegerField(db_column='DEFAULT_PRODUCT_SKU_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    product_code = models.CharField(db_column='PRODUCT_CODE', max_length=32)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    min_order_quantity = models.IntegerField(db_column='MIN_ORDER_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    max_order_quantity = models.IntegerField(db_column='MAX_ORDER_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    image_url = models.CharField(db_column='IMAGE_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    meta_title = models.CharField(db_column='META_TITLE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    meta_keyword = models.CharField(db_column='META_KEYWORD', max_length=256, blank=True, null=True)  # Field name made lowercase.
    meta_description = models.CharField(db_column='META_DESCRIPTION', max_length=256, blank=True, null=True)  # Field name made lowercase.
    template_path = models.CharField(db_column='TEMPLATE_PATH', max_length=128, blank=True, null=True)  # Field name made lowercase.
    shelve_time = models.DateTimeField(db_column='SHELVE_TIME', blank=True, null=True)  # Field name made lowercase.
    off_shelve_time = models.DateTimeField(db_column='OFF_SHELVE_TIME', blank=True, null=True)  # Field name made lowercase.
    redirect_url = models.CharField(db_column='REDIRECT_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    need_shipment = models.IntegerField(db_column='NEED_SHIPMENT', blank=True, null=True)  # Field name made lowercase.
    tags = models.CharField(db_column='TAGS', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    promotion_tags = models.CharField(db_column='PROMOTION_TAGS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    sku_options = models.CharField(db_column='SKU_OPTIONS', max_length=500, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product'


class TBaseProductExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    m_description = models.TextField(db_column='M_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product_ext'


class TBaseProductImage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    pic_type = models.IntegerField(db_column='PIC_TYPE', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    car_color_id = models.IntegerField(db_column='CAR_COLOR_ID', blank=True, null=True)  # Field name made lowercase.
    pic_size = models.CharField(db_column='PIC_SIZE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    position = models.IntegerField(db_column='POSITION', blank=True, null=True)  # Field name made lowercase.
    localfilepath = models.CharField(db_column='LOCALFILEPATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cdnpath = models.CharField(db_column='CDNPATH', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    visit = models.IntegerField(db_column='VISIT', blank=True, null=True)  # Field name made lowercase.
    image_order = models.IntegerField(db_column='IMAGE_ORDER', blank=True, null=True)  # Field name made lowercase.
    show_target = models.CharField(db_column='SHOW_TARGET', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pub_date = models.CharField(db_column='PUB_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product_image'


class TBaseProductProperty(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    property_group_id = models.IntegerField(db_column='PROPERTY_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    property_name = models.CharField(db_column='PROPERTY_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property_code = models.CharField(db_column='PROPERTY_CODE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property_default_value = models.CharField(db_column='PROPERTY_DEFAULT_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property_type = models.SmallIntegerField(db_column='PROPERTY_TYPE', blank=True, null=True)  # Field name made lowercase.
    property_data_type = models.SmallIntegerField(db_column='PROPERTY_DATA_TYPE', blank=True, null=True)  # Field name made lowercase.
    property_business_type = models.IntegerField(db_column='PROPERTY_BUSINESS_TYPE', blank=True, null=True)  # Field name made lowercase.
    property_options = models.CharField(db_column='PROPERTY_OPTIONS', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    property_event = models.CharField(db_column='PROPERTY_EVENT', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    property_ext_value = models.CharField(db_column='PROPERTY_EXT_VALUE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    is_mandatory = models.IntegerField(db_column='IS_MANDATORY', blank=True, null=True)  # Field name made lowercase.
    is_sku = models.IntegerField(db_column='IS_SKU', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product_property'


class TBaseProductPropertyGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='GROUP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    business_type = models.IntegerField(db_column='BUSINESS_TYPE', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product_property_group'


class TBaseProductVideo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(db_column='KEYWORDS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    videos = models.CharField(db_column='VIDEOS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    thumb = models.CharField(db_column='THUMB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pub_date = models.DateTimeField(db_column='PUB_DATE', blank=True, null=True)  # Field name made lowercase.
    video_count = models.IntegerField(db_column='VIDEO_COUNT', blank=True, null=True)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    edit_time = models.DateTimeField(db_column='EDIT_TIME', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_product_video'


class TBasePropertyGroupItem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    property_group_id = models.IntegerField(db_column='PROPERTY_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    property_id = models.IntegerField(db_column='PROPERTY_ID', blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    category_id = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    item_type = models.IntegerField(db_column='ITEM_TYPE', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_property_group_item'


class TBasePropertyValue(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    property_id = models.IntegerField(db_column='PROPERTY_ID', blank=True, null=True)  # Field name made lowercase.
    property_group_item_id = models.IntegerField(db_column='PROPERTY_GROUP_ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    short_text = models.CharField(db_column='SHORT_TEXT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    long_text = models.TextField(db_column='LONG_TEXT', blank=True, null=True)  # Field name made lowercase.
    int_value = models.IntegerField(db_column='INT_VALUE', blank=True, null=True)  # Field name made lowercase.
    decimal_value = models.DecimalField(db_column='DECIMAL_VALUE', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    boolean_value = models.SmallIntegerField(db_column='BOOLEAN_VALUE', blank=True, null=True)  # Field name made lowercase.
    date_value = models.DateTimeField(db_column='DATE_VALUE', blank=True, null=True)  # Field name made lowercase.
    url_value = models.CharField(db_column='URL_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    icon_value = models.CharField(db_column='ICON_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color_value = models.CharField(db_column='COLOR_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_property_value'


class TBaseProvince(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    province_id = models.CharField(db_column='PROVINCE_ID', max_length=36)  # Field name made lowercase.
    province_code = models.CharField(db_column='PROVINCE_CODE', max_length=50)  # Field name made lowercase.
    province_name = models.CharField(db_column='PROVINCE_NAME', max_length=100)  # Field name made lowercase.
    province_alias = models.CharField(db_column='PROVINCE_ALIAS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    province_initial = models.CharField(db_column='PROVINCE_INITIAL', max_length=10, blank=True, null=True)  # Field name made lowercase.
    region_id = models.IntegerField(db_column='REGION_ID', blank=True, null=True)  # Field name made lowercase.
    regionalism_code = models.CharField(db_column='REGIONALISM_CODE', max_length=36, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=32)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=32)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_province'


class TBaseRegion(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    region_name = models.CharField(db_column='REGION_NAME', max_length=100)  # Field name made lowercase.
    region_alias = models.CharField(db_column='REGION_ALIAS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_show = models.CharField(db_column='IS_SHOW', max_length=2, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=255)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_region'


class TBaseSmallCarType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    small_car_type_id = models.CharField(db_column='SMALL_CAR_TYPE_ID', max_length=36)  # Field name made lowercase.
    std_car_id = models.CharField(db_column='STD_CAR_ID', max_length=36)  # Field name made lowercase.
    small_car_type_code = models.CharField(db_column='SMALL_CAR_TYPE_CODE', max_length=50)  # Field name made lowercase.
    small_car_type_cn = models.CharField(db_column='SMALL_CAR_TYPE_CN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    small_car_type_en = models.CharField(db_column='SMALL_CAR_TYPE_EN', max_length=100, blank=True, null=True)  # Field name made lowercase.
    car_brand_code = models.CharField(db_column='CAR_BRAND_CODE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_small_car_type'


class TBaseSmallarea(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    small_area_id = models.CharField(db_column='SMALL_AREA_ID', max_length=36)  # Field name made lowercase.
    big_area_id = models.CharField(db_column='BIG_AREA_ID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    small_area_name = models.CharField(db_column='SMALL_AREA_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    order_no = models.IntegerField(db_column='ORDER_NO', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.CharField(db_column='IS_ENABLE', max_length=2)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_smallarea'


class TBaseSystemInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    corp_name = models.CharField(db_column='CORP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_logo = models.CharField(db_column='CORP_LOGO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_email = models.CharField(db_column='CORP_EMAIL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_phone = models.CharField(db_column='CORP_PHONE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_fax = models.CharField(db_column='CORP_FAX', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_qq = models.CharField(db_column='CORP_QQ', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_hotline = models.CharField(db_column='CORP_HOTLINE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_address = models.CharField(db_column='CORP_ADDRESS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    corp_zip = models.CharField(db_column='CORP_ZIP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indexmeta_keyword = models.CharField(db_column='INDEXMETA_KEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indexmeta_description = models.CharField(db_column='INDEXMETA_DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    indexmeta_title = models.CharField(db_column='INDEXMETA_TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_system_info'


class TBaseSystemPubInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    sys_id = models.IntegerField(db_column='SYS_ID', blank=True, null=True)  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='TYPE', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT', blank=True, null=True)  # Field name made lowercase.
    pub_info_url = models.CharField(db_column='PUB_INFO_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_system_pub_info'


class TBaseTmallMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID')  # Field name made lowercase.
    alipay_id = models.CharField(db_column='ALIPAY_ID', max_length=17, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_tmall_member'


class TBaseWechatMember(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID')  # Field name made lowercase.
    union_id = models.CharField(db_column='UNION_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    headimgurl = models.CharField(db_column='HEADIMGURL', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    wx_area = models.CharField(db_column='WX_AREA', max_length=64, blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_base_wechat_member'


class TCmsArticle(models.Model):
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    front_img_path = models.CharField(max_length=500)
    source = models.CharField(max_length=255)
    description = models.TextField()
    content = models.TextField()
    add_link = models.CharField(max_length=255)
    status = models.CharField(max_length=10)
    creator = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modifier = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    sort_order = models.IntegerField()
    section_id = models.IntegerField()
    trans_content = models.TextField(blank=True, null=True)
    img_all_src = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_article'


class TCmsArticleRela(models.Model):
    article_id = models.IntegerField()
    type = models.CharField(max_length=20)
    object_id = models.IntegerField()
    object_name = models.CharField(max_length=255)
    creator = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modifier = models.CharField(max_length=255)
    update_date = models.DateTimeField()
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_cms_article_rela'


class TCmsCataAttrs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cata_id = models.IntegerField()
    enname = models.CharField(max_length=255)
    cnname = models.CharField(max_length=255)
    datatype = models.IntegerField()
    value = models.CharField(max_length=255)
    length = models.FloatField()
    isnull = models.IntegerField()
    min = models.DecimalField(max_digits=10, decimal_places=2)
    max = models.DecimalField(max_digits=10, decimal_places=2)
    boxmode = models.IntegerField()
    serialids = models.CharField(max_length=500)
    serialvalues = models.CharField(max_length=500)
    remark = models.CharField(max_length=255)
    creator = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    updated_date = models.DateTimeField()
    is_enable = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_cata_attrs'


class TCmsCatalogs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cata_name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)
    parent_id = models.CharField(max_length=255)
    pc_display = models.IntegerField()
    mobile_display = models.IntegerField()
    vieworder = models.IntegerField()
    model_id = models.IntegerField()
    model_table = models.CharField(max_length=255)
    model_instanceid = models.IntegerField()
    cata_attr_type = models.IntegerField()
    cata_type_id = models.IntegerField()
    cata_alias = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    futitle = models.CharField(max_length=255)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    url_pattern = models.CharField(max_length=255)
    pc_template = models.CharField(max_length=255)
    mobile_template = models.CharField(max_length=255)
    pc_content_template = models.CharField(max_length=255)
    mobile_content_template = models.CharField(max_length=255)
    is_enable = models.IntegerField()
    creator = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modifier = models.CharField(max_length=255)
    updated_date = models.DateTimeField()
    cata_full_alias = models.CharField(max_length=255, blank=True, null=True)
    as_search_result = models.IntegerField(blank=True, null=True)
    cata_full_alias_path = models.CharField(max_length=500, blank=True, null=True)
    cata_name_path = models.CharField(max_length=500, blank=True, null=True)
    rela_table = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_catalogs'


class TCmsCatatype(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    type_name = models.CharField(db_column='TYPE_NAME', max_length=255)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=255)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_cms_catatype'


class TCmsCatatypeAttrs(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    cata_type_id = models.IntegerField(db_column='CATA_TYPE_ID')  # Field name made lowercase.
    enname = models.CharField(db_column='ENNAME', max_length=255)  # Field name made lowercase.
    cnname = models.CharField(db_column='CNNAME', max_length=255)  # Field name made lowercase.
    datatype = models.IntegerField(db_column='DATATYPE')  # Field name made lowercase.
    length = models.FloatField(db_column='LENGTH')  # Field name made lowercase.
    isnull = models.IntegerField(db_column='ISNULL')  # Field name made lowercase.
    min = models.DecimalField(db_column='MIN', max_digits=10, decimal_places=2)  # Field name made lowercase.
    max = models.DecimalField(db_column='MAX', max_digits=10, decimal_places=2)  # Field name made lowercase.
    boxmode = models.CharField(db_column='BOXMODE', max_length=255)  # Field name made lowercase.
    serialids = models.CharField(db_column='SERIALIDS', max_length=500)  # Field name made lowercase.
    serialvalues = models.CharField(db_column='SERIALVALUES', max_length=500)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_cms_catatype_attrs'


class TCmsLinkword(models.Model):
    word = models.CharField(max_length=50)
    link = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    creator = models.CharField(max_length=255)
    created_date = models.DateTimeField()
    modifier = models.CharField(max_length=255)
    update_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_cms_linkword'


class TCmsModels(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    model_name = models.CharField(max_length=255)
    model_table = models.CharField(max_length=255)
    id_field = models.CharField(max_length=255)
    name_filed = models.CharField(max_length=255)
    remark = models.CharField(max_length=255)
    is_enable = models.IntegerField()
    rela_table = models.CharField(max_length=255, blank=True, null=True)
    rela_id_field = models.CharField(max_length=255, blank=True, null=True)
    rela_name_field = models.CharField(max_length=255, blank=True, null=True)
    rela_extra_field = models.CharField(max_length=255, blank=True, null=True)
    rela_foreign_field = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    updated_date = models.DateTimeField()
    model_instanceid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_models'


class TCmsSection(models.Model):
    parent_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    cata_id = models.IntegerField(blank=True, null=True)
    pc_template_id = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField()
    sort_order = models.IntegerField(blank=True, null=True)
    id_path = models.CharField(max_length=500, blank=True, null=True)
    name_path = models.CharField(max_length=500, blank=True, null=True)
    mobile_template_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_section'


class TCmsTemplate(models.Model):
    template_name = models.CharField(max_length=100, blank=True, null=True)
    template_path = models.CharField(max_length=255, blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    modifier = models.CharField(max_length=255, blank=True, null=True)
    update_date = models.DateTimeField()
    template_type = models.CharField(max_length=30, blank=True, null=True)
    template_teriminal = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_cms_template'


class TE4SDbCustomerAccount(models.Model):
    customer_id = models.CharField(db_column='CUSTOMER_ID', unique=True, max_length=32)  # Field name made lowercase.
    customer_name = models.CharField(db_column='CUSTOMER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=8, blank=True, null=True)  # Field name made lowercase.
    activation_status = models.CharField(db_column='ACTIVATION_STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=1, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=64, blank=True, null=True)  # Field name made lowercase.
    question = models.CharField(db_column='QUESTION', max_length=128, blank=True, null=True)  # Field name made lowercase.
    answer = models.CharField(db_column='ANSWER', max_length=128, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    mobile = models.CharField(max_length=32, blank=True, null=True)
    nick_name = models.CharField(max_length=64, blank=True, null=True)
    orgid = models.CharField(db_column='ORGID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    activating_key = models.CharField(db_column='ACTIVATING_KEY', max_length=32, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    searchpwd_key = models.CharField(db_column='SEARCHPWD_KEY', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reset_email = models.CharField(db_column='RESET_EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    reset_mobile = models.CharField(db_column='RESET_MOBILE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pwd_safe_factor = models.CharField(db_column='PWD_SAFE_FACTOR', max_length=8, blank=True, null=True)  # Field name made lowercase.
    binding_email = models.CharField(db_column='BINDING_EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    reset_binding_email = models.CharField(db_column='RESET_BINDING_EMAIL', max_length=128, blank=True, null=True)  # Field name made lowercase.
    guide_step = models.CharField(db_column='GUIDE_STEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    sub_guide_step = models.CharField(db_column='SUB_GUIDE_STEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    open_guide_step = models.CharField(db_column='OPEN_GUIDE_STEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    level_up_step = models.CharField(db_column='LEVEL_UP_STEP', max_length=8, blank=True, null=True)  # Field name made lowercase.
    information_source = models.CharField(db_column='INFORMATION_SOURCE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    application_status = models.CharField(db_column='APPLICATION_STATUS', max_length=8, blank=True, null=True)  # Field name made lowercase.
    domain = models.CharField(db_column='DOMAIN', max_length=256, blank=True, null=True)  # Field name made lowercase.
    application_id = models.CharField(db_column='APPLICATION_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    blacklist = models.IntegerField(db_column='BLACKLIST', blank=True, null=True)  # Field name made lowercase.
    internal_account = models.CharField(max_length=64, blank=True, null=True)
    trade_password = models.CharField(db_column='TRADE_PASSWORD', max_length=60, blank=True, null=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    pay_pwd = models.CharField(db_column='PAY_PWD', max_length=64, blank=True, null=True)  # Field name made lowercase.
    paypwd_safe_factor = models.CharField(db_column='PAYPWD_SAFE_FACTOR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    guide_id = models.CharField(db_column='GUIDE_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    crm_user_id = models.CharField(db_column='CRM_USER_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    user_version = models.CharField(db_column='USER_VERSION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    emp_pic = models.CharField(db_column='EMP_PIC', max_length=500, blank=True, null=True)  # Field name made lowercase.
    gender_code = models.CharField(db_column='GENDER_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    real_name = models.CharField(db_column='REAL_NAME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emp_code = models.CharField(db_column='EMP_CODE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_contract_status = models.CharField(db_column='CUSTOMER_CONTRACT_STATUS', max_length=2, blank=True, null=True)  # Field name made lowercase.
    wechat_openid = models.CharField(db_column='WECHAT_OPENID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zfb_openid = models.CharField(db_column='ZFB_OPENID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    last_update_date = models.DateTimeField(db_column='LAST_UPDATE_DATE', blank=True, null=True)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_customer_account'


class TE4SDbDictionaryData(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dict_type_id = models.IntegerField(db_column='DICT_TYPE_ID')  # Field name made lowercase.
    dict_data_code = models.CharField(db_column='DICT_DATA_CODE', max_length=32)  # Field name made lowercase.
    dict_data_name = models.CharField(db_column='DICT_DATA_NAME', max_length=64)  # Field name made lowercase.
    ordering = models.IntegerField(db_column='ORDERING')  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_dictionary_data'


class TE4SDbDictionaryType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dict_type_code = models.CharField(db_column='DICT_TYPE_CODE', max_length=32)  # Field name made lowercase.
    dict_type_name = models.CharField(db_column='DICT_TYPE_NAME', max_length=32)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_dictionary_type'


class TE4SDbFunction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    parent_id = models.IntegerField(db_column='PARENT_ID', blank=True, null=True)  # Field name made lowercase.
    function_code = models.CharField(db_column='FUNCTION_CODE', max_length=64, blank=True, null=True)  # Field name made lowercase.
    function_name = models.CharField(db_column='FUNCTION_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    function_type = models.CharField(db_column='FUNCTION_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    page_link = models.CharField(db_column='PAGE_LINK', max_length=128, blank=True, null=True)  # Field name made lowercase.
    icon_class = models.CharField(db_column='ICON_CLASS', max_length=20, blank=True, null=True)  # Field name made lowercase.
    ordering = models.IntegerField(db_column='ORDERING', blank=True, null=True)  # Field name made lowercase.
    layer = models.IntegerField(db_column='LAYER', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    authc_link = models.CharField(db_column='AUTHC_LINK', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_function'


class TE4SDbLogMessage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='CLASS_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    method_name = models.CharField(db_column='METHOD_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    method_params = models.TextField(db_column='METHOD_PARAMS', blank=True, null=True)  # Field name made lowercase.
    log_date = models.DateTimeField(db_column='LOG_DATE', blank=True, null=True)  # Field name made lowercase.
    log_message = models.TextField(db_column='LOG_MESSAGE', blank=True, null=True)  # Field name made lowercase.
    operation_type = models.CharField(db_column='OPERATION_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    remark = models.TextField(db_column='REMARK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_log_message'


class TE4SDbLogRegister(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    function_id = models.IntegerField(db_column='FUNCTION_ID', blank=True, null=True)  # Field name made lowercase.
    operation_type = models.CharField(db_column='OPERATION_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    class_name = models.CharField(db_column='CLASS_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_log_register'


class TE4SDbPasswordHistory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=32)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=64)  # Field name made lowercase.
    create_date = models.DateTimeField(db_column='CREATE_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_password_history'


class TE4SDbRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_code = models.CharField(db_column='ROLE_CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    role_name = models.CharField(db_column='ROLE_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='STATE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    store_id = models.CharField(db_column='STORE_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    role_type = models.IntegerField(db_column='ROLE_TYPE', blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_role'


class TE4SDbRoleFunction(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    function_id = models.IntegerField(db_column='FUNCTION_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_role_function'


class TE4SDbUser(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    login_name = models.CharField(db_column='LOGIN_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=128, blank=True, null=True)  # Field name made lowercase.
    salt = models.CharField(db_column='SALT', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_state = models.CharField(db_column='USER_STATE', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_user'


class TE4SDbUserInfo(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID', blank=True, null=True)  # Field name made lowercase.
    login_name = models.CharField(db_column='LOGIN_NAME', max_length=32)  # Field name made lowercase.
    user_name = models.CharField(db_column='USER_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(db_column='PASSWORD', max_length=128)  # Field name made lowercase.
    salt = models.CharField(db_column='SALT', max_length=64, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=32, blank=True, null=True)  # Field name made lowercase.
    mobile_phone = models.CharField(db_column='MOBILE_PHONE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_type = models.CharField(db_column='USER_TYPE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    dlr_code = models.CharField(db_column='DLR_CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_role_id = models.IntegerField(db_column='LAST_ROLE_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE', blank=True, null=True)  # Field name made lowercase.
    remark = models.CharField(db_column='REMARK', max_length=256, blank=True, null=True)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_user_info'


class TE4SDbUserRole(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=32)  # Field name made lowercase.
    role_id = models.IntegerField(db_column='ROLE_ID')  # Field name made lowercase.
    manager_id = models.CharField(db_column='MANAGER_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    user_id = models.IntegerField(db_column='USER_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_db_user_role'


class TE4SWcServer(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=32)  # Field name made lowercase.
    server_head = models.CharField(db_column='SERVER_HEAD', max_length=128, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=64)  # Field name made lowercase.
    nick_name = models.CharField(db_column='NICK_NAME', max_length=64)  # Field name made lowercase.
    server_sign = models.CharField(db_column='SERVER_SIGN', max_length=256, blank=True, null=True)  # Field name made lowercase.
    personal_greeting = models.CharField(db_column='PERSONAL_GREETING', max_length=512, blank=True, null=True)  # Field name made lowercase.
    server_group_id = models.CharField(db_column='SERVER_GROUP_ID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    km_accout = models.CharField(db_column='KM_ACCOUT', max_length=32, blank=True, null=True)  # Field name made lowercase.
    auto_reply_time = models.CharField(db_column='AUTO_REPLY_TIME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    auto_reply_content = models.CharField(db_column='AUTO_REPLY_CONTENT', max_length=512, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_e4s_wc_server'


class TEcommerceCardPayment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    orderpayment_id = models.IntegerField(db_column='ORDERPAYMENT_ID', blank=True, null=True)  # Field name made lowercase.
    card_id = models.IntegerField(db_column='CARD_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_card_payment'


class TEcommerceComment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordersku_id = models.IntegerField(db_column='ORDERSKU_ID', blank=True, null=True)  # Field name made lowercase.
    com_date = models.CharField(db_column='COM_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    comment_next = models.IntegerField(db_column='COMMENT_NEXT', blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE', blank=True, null=True)  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_comment'


class TEcommerceCommodity(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_code = models.CharField(db_column='COMMODITY_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    inventory_id = models.IntegerField(db_column='INVENTORY_ID', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    date_from = models.DateTimeField(db_column='DATE_FROM', blank=True, null=True)  # Field name made lowercase.
    date_to = models.DateTimeField(db_column='DATE_TO', blank=True, null=True)  # Field name made lowercase.
    period = models.IntegerField(db_column='PERIOD', blank=True, null=True)  # Field name made lowercase.
    org_price = models.IntegerField(db_column='ORG_PRICE', blank=True, null=True)  # Field name made lowercase.
    off_price = models.IntegerField(db_column='OFF_PRICE', blank=True, null=True)  # Field name made lowercase.
    sale_price = models.IntegerField(db_column='SALE_PRICE', blank=True, null=True)  # Field name made lowercase.
    order_price = models.IntegerField(db_column='ORDER_PRICE', blank=True, null=True)  # Field name made lowercase.
    sales_total = models.IntegerField(db_column='SALES_TOTAL', blank=True, null=True)  # Field name made lowercase.
    restriction_total = models.IntegerField(db_column='RESTRICTION_TOTAL', blank=True, null=True)  # Field name made lowercase.
    tag = models.CharField(db_column='TAG', max_length=255, blank=True, null=True)  # Field name made lowercase.
    propertyvalueinfos = models.TextField(db_column='PROPERTYVALUEINFOS', blank=True, null=True)  # Field name made lowercase.
    metakeyword = models.CharField(db_column='METAKEYWORD', max_length=255, blank=True, null=True)  # Field name made lowercase.
    metadescription = models.CharField(db_column='METADESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    gen_clue = models.IntegerField(db_column='GEN_CLUE', blank=True, null=True)  # Field name made lowercase.
    redirect_url = models.CharField(db_column='REDIRECT_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION', blank=True, null=True)  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity'


class TEcommerceCommodityCarExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    car_series_id = models.IntegerField(db_column='CAR_SERIES_ID', blank=True, null=True)  # Field name made lowercase.
    car_model_id = models.IntegerField(db_column='CAR_MODEL_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_car_ext'


class TEcommerceCommodityDealer(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    big_area_id = models.IntegerField(db_column='BIG_AREA_ID', blank=True, null=True)  # Field name made lowercase.
    small_area_id = models.IntegerField(db_column='SMALL_AREA_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_dealer'


class TEcommerceCommodityExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    title_mini = models.CharField(db_column='TITLE_MINI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pic = models.CharField(db_column='PIC', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pic_mini = models.CharField(db_column='PIC_MINI', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    m_description = models.TextField(db_column='M_DESCRIPTION', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_ext'


class TEcommerceCommodityInventory(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    quantity_onhand = models.IntegerField(db_column='QUANTITY_ONHAND', blank=True, null=True)  # Field name made lowercase.
    allocated_quantity = models.IntegerField(db_column='ALLOCATED_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    reorder_minimnm = models.IntegerField(db_column='REORDER_MINIMNM', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_inventory'


class TEcommerceCommoditySku(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    product_id = models.IntegerField(db_column='PRODUCT_ID', blank=True, null=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    car_color_id = models.IntegerField(db_column='CAR_COLOR_ID', blank=True, null=True)  # Field name made lowercase.
    property_id = models.IntegerField(db_column='PROPERTY_ID', blank=True, null=True)  # Field name made lowercase.
    property_value_id = models.IntegerField(db_column='PROPERTY_VALUE_ID', blank=True, null=True)  # Field name made lowercase.
    sku_name = models.CharField(db_column='SKU_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sku_value = models.CharField(db_column='SKU_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sku_icon = models.CharField(db_column='SKU_ICON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sku_redirect_url = models.CharField(db_column='SKU_REDIRECT_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_sku'


class TEcommerceCommodityVerifyExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    logo_url = models.CharField(db_column='LOGO_URL', max_length=255, blank=True, null=True)  # Field name made lowercase.
    code_type = models.CharField(db_column='CODE_TYPE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='COLOR', max_length=64, blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=27, blank=True, null=True)  # Field name made lowercase.
    sub_title = models.CharField(db_column='SUB_TITLE', max_length=54, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    card_type = models.CharField(db_column='CARD_TYPE', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    need_verified = models.IntegerField(db_column='NEED_VERIFIED', blank=True, null=True)  # Field name made lowercase.
    verified = models.CharField(db_column='VERIFIED', max_length=255, blank=True, null=True)  # Field name made lowercase.
    verified_from = models.DateTimeField(db_column='VERIFIED_FROM', blank=True, null=True)  # Field name made lowercase.
    verified_to = models.DateTimeField(db_column='VERIFIED_TO', blank=True, null=True)  # Field name made lowercase.
    fixed_term = models.IntegerField(db_column='FIXED_TERM', blank=True, null=True)  # Field name made lowercase.
    fixed_begin_term = models.IntegerField(db_column='FIXED_BEGIN_TERM', blank=True, null=True)  # Field name made lowercase.
    reconciliation_clearing = models.CharField(db_column='RECONCILIATION_CLEARING', max_length=2000, blank=True, null=True)  # Field name made lowercase.
    card_id = models.CharField(db_column='CARD_ID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE', blank=True, null=True)  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_commodity_verify_ext'


class TEcommerceCoupon(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_group_id = models.IntegerField(db_column='COUPON_GROUP_ID', blank=True, null=True)  # Field name made lowercase.
    show_name = models.CharField(db_column='SHOW_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    coupon_type = models.IntegerField(db_column='COUPON_TYPE', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    valid_period = models.IntegerField(db_column='VALID_PERIOD', blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    repeat = models.IntegerField(db_column='REPEAT', blank=True, null=True)  # Field name made lowercase.
    double_discounting = models.IntegerField(db_column='DOUBLE_DISCOUNTING', blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='CONDITION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_coupon'


class TEcommerceCouponCard(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_id = models.IntegerField(db_column='COUPON_ID', blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    gift_certificateno = models.CharField(db_column='GIFT_CERTIFICATENO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    secret = models.CharField(db_column='SECRET', max_length=255, blank=True, null=True)  # Field name made lowercase.
    expire = models.DateTimeField(db_column='EXPIRE', blank=True, null=True)  # Field name made lowercase.
    gen_date = models.DateTimeField(db_column='GEN_DATE', blank=True, null=True)  # Field name made lowercase.
    use_date = models.DateTimeField(db_column='USE_DATE', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_coupon_card'


class TEcommerceCouponGroup(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    coupon_group_name = models.CharField(db_column='COUPON_GROUP_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    total = models.IntegerField(db_column='TOTAL', blank=True, null=True)  # Field name made lowercase.
    dicount_total = models.IntegerField(db_column='DICOUNT_TOTAL', blank=True, null=True)  # Field name made lowercase.
    discount_percentage = models.IntegerField(db_column='DISCOUNT_PERCENTAGE', blank=True, null=True)  # Field name made lowercase.
    condition = models.CharField(db_column='CONDITION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active_date = models.DateTimeField(db_column='ACTIVE_DATE', blank=True, null=True)  # Field name made lowercase.
    expire_date = models.DateTimeField(db_column='EXPIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_coupon_group'


class TEcommerceFinacialOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    item_id = models.IntegerField(db_column='ITEM_ID', blank=True, null=True)  # Field name made lowercase.
    license_type = models.IntegerField(db_column='LICENSE_TYPE', blank=True, null=True)  # Field name made lowercase.
    license_no = models.CharField(db_column='LICENSE_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    job = models.CharField(db_column='JOB', max_length=255, blank=True, null=True)  # Field name made lowercase.
    income = models.CharField(db_column='INCOME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    insurance = models.CharField(db_column='INSURANCE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    reservefund = models.CharField(db_column='RESERVEFUND', max_length=255, blank=True, null=True)  # Field name made lowercase.
    self_credit = models.CharField(db_column='SELF_CREDIT', max_length=255, blank=True, null=True)  # Field name made lowercase.
    house = models.CharField(db_column='HOUSE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    credit_status = models.CharField(db_column='CREDIT_STATUS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_finacial_order'


class TEcommerceOrder(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=11, blank=True, null=True)  # Field name made lowercase.
    member_id = models.IntegerField(db_column='MEMBER_ID', blank=True, null=True)  # Field name made lowercase.
    open_id = models.CharField(db_column='OPEN_ID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    orderaddressid = models.IntegerField(db_column='ORDERADDRESSID', blank=True, null=True)  # Field name made lowercase.
    order_type = models.IntegerField(db_column='ORDER_TYPE', blank=True, null=True)  # Field name made lowercase.
    order_no = models.CharField(db_column='ORDER_NO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE', blank=True, null=True)  # Field name made lowercase.
    source = models.IntegerField(db_column='SOURCE', blank=True, null=True)  # Field name made lowercase.
    contact_id = models.CharField(db_column='CONTACT_ID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    extra_info = models.CharField(db_column='EXTRA_INFO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order'


class TEcommerceOrderAddress(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    region_id = models.IntegerField(db_column='REGION_ID', blank=True, null=True)  # Field name made lowercase.
    region_fullname = models.CharField(db_column='REGION_FULLNAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phone_number = models.CharField(db_column='PHONE_NUMBER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    fax_number = models.CharField(db_column='FAX_NUMBER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    postal_code = models.CharField(db_column='POSTAL_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address1 = models.CharField(db_column='ADDRESS1', max_length=128, blank=True, null=True)  # Field name made lowercase.
    address2 = models.CharField(db_column='ADDRESS2', max_length=128, blank=True, null=True)  # Field name made lowercase.
    contact_full_name = models.CharField(db_column='CONTACT_FULL_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    contact_mobile = models.CharField(db_column='CONTACT_MOBILE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_address'


class TEcommerceOrderFlowstatus(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    status = models.IntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    pay_status = models.IntegerField(db_column='PAY_STATUS', blank=True, null=True)  # Field name made lowercase.
    info = models.CharField(db_column='INFO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_flowstatus'


class TEcommerceOrderPayment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID')  # Field name made lowercase.
    document_no = models.CharField(db_column='DOCUMENT_NO', unique=True, max_length=32)  # Field name made lowercase.
    document_type = models.SmallIntegerField(db_column='DOCUMENT_TYPE')  # Field name made lowercase.
    payment_amount = models.DecimalField(db_column='PAYMENT_AMOUNT', max_digits=12, decimal_places=2)  # Field name made lowercase.
    commission = models.DecimalField(db_column='COMMISSION', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    paymentgateway_name = models.TextField(db_column='PAYMENTGATEWAY_NAME', blank=True, null=True)  # Field name made lowercase.
    paymentgateway_id = models.IntegerField(db_column='PAYMENTGATEWAY_ID', blank=True, null=True)  # Field name made lowercase.
    payment_type = models.SmallIntegerField(db_column='PAYMENT_TYPE', blank=True, null=True)  # Field name made lowercase.
    paymenttype_desc = models.TextField(db_column='PAYMENTTYPE_DESC', blank=True, null=True)  # Field name made lowercase.
    has_invoice = models.SmallIntegerField(db_column='HAS_INVOICE')  # Field name made lowercase.
    invoice_title = models.CharField(db_column='INVOICE_TITLE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    ip_address = models.CharField(db_column='IP_ADDRESS', max_length=64, blank=True, null=True)  # Field name made lowercase.
    gift_certificateno = models.CharField(db_column='GIFT_CERTIFICATENO', max_length=32, blank=True, null=True)  # Field name made lowercase.
    used_shoppoint = models.IntegerField(db_column='USED_SHOPPOINT', blank=True, null=True)  # Field name made lowercase.
    account_info = models.TextField(db_column='ACCOUNT_INFO', blank=True, null=True)  # Field name made lowercase.
    return_reason = models.TextField(db_column='RETURN_REASON', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.
    payer = models.CharField(db_column='PAYER', max_length=32, blank=True, null=True)  # Field name made lowercase.
    payee = models.CharField(db_column='PAYEE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    pay_time = models.CharField(db_column='PAY_TIME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_payment'


class TEcommerceOrderShipment(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID')  # Field name made lowercase.
    document_type = models.SmallIntegerField(db_column='DOCUMENT_TYPE')  # Field name made lowercase.
    shippingaddress_id = models.IntegerField(db_column='SHIPPINGADDRESS_ID', blank=True, null=True)  # Field name made lowercase.
    document_no = models.CharField(db_column='DOCUMENT_NO', unique=True, max_length=32)  # Field name made lowercase.
    tracking_no = models.CharField(db_column='TRACKING_NO', max_length=128, blank=True, null=True)  # Field name made lowercase.
    wrap_cost = models.IntegerField(db_column='WRAP_COST', blank=True, null=True)  # Field name made lowercase.
    wrap_id = models.IntegerField(db_column='WRAP_ID', blank=True, null=True)  # Field name made lowercase.
    wrap_name = models.CharField(db_column='WRAP_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    carrier_code = models.CharField(db_column='CARRIER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    carrier_name = models.CharField(db_column='CARRIER_NAME', max_length=128, blank=True, null=True)  # Field name made lowercase.
    shipping_cost = models.IntegerField(db_column='SHIPPING_COST', blank=True, null=True)  # Field name made lowercase.
    shippingmethod_id = models.IntegerField(db_column='SHIPPINGMETHOD_ID', blank=True, null=True)  # Field name made lowercase.
    shippingrate_id = models.IntegerField(db_column='SHIPPINGRATE_ID', blank=True, null=True)  # Field name made lowercase.
    delivery_time = models.CharField(db_column='DELIVERY_TIME', max_length=32, blank=True, null=True)  # Field name made lowercase.
    needconfrim_b4delivery = models.SmallIntegerField(db_column='NEEDCONFRIM_B4DELIVERY', blank=True, null=True)  # Field name made lowercase.
    selfcollectioncentre_id = models.IntegerField(db_column='SELFCOLLECTIONCENTRE_ID', blank=True, null=True)  # Field name made lowercase.
    selfcollectioncentre_name = models.CharField(db_column='SELFCOLLECTIONCENTRE_NAME', max_length=64, blank=True, null=True)  # Field name made lowercase.
    exceptedselfcollect_date = models.CharField(db_column='EXCEPTEDSELFCOLLECT_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    actualselfcollect_date = models.CharField(db_column='ACTUALSELFCOLLECT_DATE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    need_interface = models.IntegerField(db_column='NEED_INTERFACE', blank=True, null=True)  # Field name made lowercase.
    vin = models.CharField(db_column='VIN', max_length=128, blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_shipment'


class TEcommerceOrderShipmentExt(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shipment_id = models.IntegerField(db_column='SHIPMENT_ID')  # Field name made lowercase.
    wrap_note = models.TextField(db_column='WRAP_NOTE', blank=True, null=True)  # Field name made lowercase.
    deliverytype_desc = models.TextField(db_column='DELIVERYTYPE_DESC', blank=True, null=True)  # Field name made lowercase.
    return_reason = models.TextField(db_column='RETURN_REASON', blank=True, null=True)  # Field name made lowercase.
    shipment_message = models.TextField(db_column='SHIPMENT_MESSAGE', blank=True, null=True)  # Field name made lowercase.
    memo = models.TextField(db_column='MEMO', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_shipment_ext'


class TEcommerceOrderShipmentItem(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordershipment_id = models.IntegerField(db_column='ORDERSHIPMENT_ID')  # Field name made lowercase.
    ordersku_id = models.IntegerField(db_column='ORDERSKU_ID')  # Field name made lowercase.
    delivery_quantity = models.IntegerField(db_column='DELIVERY_QUANTITY')  # Field name made lowercase.
    incoming_quantity = models.IntegerField(db_column='INCOMING_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_shipment_item'


class TEcommerceOrderShipmentMessage(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    shipment_id = models.IntegerField(db_column='SHIPMENT_ID')  # Field name made lowercase.
    shipment_type = models.IntegerField(db_column='SHIPMENT_TYPE', blank=True, null=True)  # Field name made lowercase.
    shipment_message = models.TextField(db_column='SHIPMENT_MESSAGE', blank=True, null=True)  # Field name made lowercase.
    shipment_time = models.DateTimeField(db_column='SHIPMENT_TIME', blank=True, null=True)  # Field name made lowercase.
    state = models.SmallIntegerField(db_column='STATE', blank=True, null=True)  # Field name made lowercase.
    status = models.SmallIntegerField(db_column='STATUS', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_shipment_message'


class TEcommerceOrderSku(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    item_type = models.SmallIntegerField(db_column='ITEM_TYPE')  # Field name made lowercase.
    order_id = models.IntegerField(db_column='ORDER_ID')  # Field name made lowercase.
    commodity_id = models.IntegerField(db_column='COMMODITY_ID', blank=True, null=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=255, blank=True, null=True)  # Field name made lowercase.
    productsku_code = models.CharField(db_column='PRODUCTSKU_CODE', max_length=32, blank=True, null=True)  # Field name made lowercase.
    displaysku_options = models.CharField(db_column='DISPLAYSKU_OPTIONS', max_length=255, blank=True, null=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='QUANTITY')  # Field name made lowercase.
    price = models.IntegerField(db_column='PRICE')  # Field name made lowercase.
    is_onsale = models.SmallIntegerField(db_column='IS_ONSALE', blank=True, null=True)  # Field name made lowercase.
    is_wholesale = models.SmallIntegerField(db_column='IS_WHOLESALE', blank=True, null=True)  # Field name made lowercase.
    tax = models.IntegerField(db_column='TAX', blank=True, null=True)  # Field name made lowercase.
    tax_name = models.TextField(db_column='TAX_NAME', blank=True, null=True)  # Field name made lowercase.
    subtotal = models.DecimalField(db_column='SUBTOTAL', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    discount = models.IntegerField(db_column='DISCOUNT', blank=True, null=True)  # Field name made lowercase.
    weight = models.DecimalField(db_column='WEIGHT', max_digits=12, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    allocated_quantity = models.IntegerField(db_column='ALLOCATED_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    delivery_quantity = models.IntegerField(db_column='DELIVERY_QUANTITY', blank=True, null=True)  # Field name made lowercase.
    gross_weight = models.DecimalField(db_column='GROSS_WEIGHT', max_digits=12, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_order_sku'


class TEcommercePaymentgateway(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymentgateway_name = models.CharField(db_column='PAYMENTGATEWAY_NAME', max_length=256)  # Field name made lowercase.
    paymentgateway_detail = models.CharField(db_column='PAYMENTGATEWAY_DETAIL', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    gateway_icon = models.CharField(db_column='GATEWAY_ICON', max_length=255, blank=True, null=True)  # Field name made lowercase.
    paymentgateway_code = models.CharField(db_column='PAYMENTGATEWAY_CODE', unique=True, max_length=32)  # Field name made lowercase.
    paymentgateway_type = models.SmallIntegerField(db_column='PAYMENTGATEWAY_TYPE', blank=True, null=True)  # Field name made lowercase.
    version = models.IntegerField(db_column='VERSION')  # Field name made lowercase.
    sort_order = models.IntegerField(db_column='SORT_ORDER', blank=True, null=True)  # Field name made lowercase.
    is_show = models.IntegerField(db_column='IS_SHOW', blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_paymentgateway'


class TEcommercePaymentgatewayProperty(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    paymentgateway_id = models.IntegerField(db_column='PAYMENTGATEWAY_ID', blank=True, null=True)  # Field name made lowercase.
    property_key = models.CharField(db_column='PROPERTY_KEY', max_length=255, blank=True, null=True)  # Field name made lowercase.
    property_value = models.CharField(db_column='PROPERTY_VALUE', max_length=255, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_paymentgateway_property'


class TEcommerceVerified(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ordersku_id = models.IntegerField(db_column='ORDERSKU_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_id = models.IntegerField(db_column='DEALER_ID', blank=True, null=True)  # Field name made lowercase.
    dealer_code = models.CharField(db_column='DEALER_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    veri_code = models.CharField(db_column='VERI_CODE', max_length=128, blank=True, null=True)  # Field name made lowercase.
    veri_date = models.DateTimeField(db_column='VERI_DATE', blank=True, null=True)  # Field name made lowercase.
    veri_number = models.CharField(db_column='VERI_NUMBER', max_length=255, blank=True, null=True)  # Field name made lowercase.
    veri_status = models.IntegerField(db_column='VERI_STATUS', blank=True, null=True)  # Field name made lowercase.
    veri_logs = models.CharField(db_column='VERI_LOGS', max_length=5000, blank=True, null=True)  # Field name made lowercase.
    card_id = models.CharField(db_column='CARD_ID', max_length=128, blank=True, null=True)  # Field name made lowercase.
    is_enable = models.IntegerField(db_column='IS_ENABLE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=50)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=50)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_ecommerce_verified'


class TSmsConfigKey(models.Model):
    brand = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    bfield = models.CharField(max_length=255, blank=True, null=True)
    btype = models.CharField(max_length=255, blank=True, null=True)
    ttype = models.CharField(max_length=255, blank=True, null=True)
    ctype = models.CharField(max_length=255, blank=True, null=True)
    mtype = models.CharField(max_length=255, blank=True, null=True)
    nindex = models.CharField(max_length=255, blank=True, null=True)
    bfrom = models.CharField(max_length=255, blank=True, null=True)
    bto = models.CharField(max_length=255, blank=True, null=True)
    blong = models.CharField(max_length=255, blank=True, null=True)
    pname = models.CharField(max_length=255, blank=True, null=True)
    pfield = models.CharField(max_length=255, blank=True, null=True)
    purl = models.CharField(max_length=255, blank=True, null=True)
    powner = models.CharField(max_length=255, blank=True, null=True)
    pkey = models.CharField(max_length=255, blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sms_config_key'


class TSmsCustLoginLogs(models.Model):
    uuid = models.CharField(db_column='UUID', primary_key=True, max_length=40)  # Field name made lowercase.
    channel = models.CharField(db_column='CHANNEL', max_length=20)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=32)  # Field name made lowercase.
    mobilenumber = models.CharField(db_column='MOBILENUMBER', max_length=20)  # Field name made lowercase.
    entrykey = models.CharField(db_column='ENTRYKEY', max_length=50)  # Field name made lowercase.
    smsparams = models.CharField(db_column='SMSPARAMS', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    sendtime = models.DateTimeField(db_column='SENDTIME')  # Field name made lowercase.
    send_sms_result = models.CharField(db_column='SEND_SMS_RESULT', max_length=128, blank=True, null=True)  # Field name made lowercase.
    send_status = models.CharField(db_column='SEND_STATUS', max_length=128, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sms_cust_login_logs'


class TSmsKeyParams(models.Model):
    key_field = models.CharField(max_length=255, blank=True, null=True)
    key_options = models.CharField(max_length=255, blank=True, null=True)
    key_desc = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sms_key_params'


class TSmsTemplate(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    source = models.CharField(db_column='SOURCE', max_length=10)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=200)  # Field name made lowercase.
    content = models.CharField(db_column='CONTENT', max_length=1024)  # Field name made lowercase.
    created_date = models.DateTimeField(db_column='CREATED_DATE')  # Field name made lowercase.
    creator = models.CharField(db_column='CREATOR', max_length=20)  # Field name made lowercase.
    updated_date = models.DateTimeField(db_column='UPDATED_DATE')  # Field name made lowercase.
    modifier = models.CharField(db_column='MODIFIER', max_length=20)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_sms_template'
