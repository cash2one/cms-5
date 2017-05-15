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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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

    class Meta:
        managed = False
        db_table = 't_sync_recode'
