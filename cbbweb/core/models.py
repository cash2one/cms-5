# -*- coding: utf-8 -*-



from django.db import models


class TClueInfo(models.Model):
    auth_key = models.CharField(max_length=64, blank=True, null=True)
    action_type = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    phone = models.CharField(max_length=64, blank=True, null=True)
    store_id = models.CharField(max_length=64, blank=True, null=True)
    clue_type = models.CharField(max_length=64, blank=True, null=True)
    source = models.CharField(max_length=64, blank=True, null=True)
    car_type_id = models.CharField(max_length=64, blank=True, null=True)
    car_series_id = models.CharField(max_length=64, blank=True, null=True)
    sex = models.CharField(max_length=64, blank=True, null=True)
    dlr_code = models.CharField(max_length=64, blank=True, null=True)
    activity_id = models.CharField(max_length=64, blank=True, null=True)
    activity_name = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    province_id = models.CharField(max_length=64, blank=True, null=True)
    city_id = models.CharField(max_length=64, blank=True, null=True)
    county_id = models.CharField(max_length=64, blank=True, null=True)
    smart_code = models.CharField(max_length=64, blank=True, null=True)
    page_id = models.CharField(max_length=64, blank=True, null=True)
    kwargs_json = models.TextField(blank=True, null=True)
    result_json = models.TextField(blank=True, null=True)
    status_code = models.CharField(max_length=64, blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_clue_info'


class TSyncConfig(models.Model):
    name = models.CharField(max_length=50)
    is_enable = models.IntegerField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 't_sync_config'


class TSyncRecode(models.Model):
    name = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    len_data = models.IntegerField()
    host = models.CharField(max_length=360, blank=True, null=True)
    url = models.CharField(max_length=360, blank=True, null=True)
    sync_type = models.CharField(max_length=50, blank=True, null=True)
    params = models.CharField(max_length=360, blank=True, null=True)
    table_name = models.CharField(max_length=360, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 't_sync_recode'

