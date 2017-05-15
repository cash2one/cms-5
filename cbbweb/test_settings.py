# -*- coding: utf-8 -*-
"""
Django settings for cbbweb project.
"""
import os
from cbbweb.base_settings import BaseConfig


class Test(BaseConfig):
    DEBUG = True
    STATIC_URL = '/static/'
    CACHEING = True
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://ddf3b048df22494a:PVuser201510@ddf3b048df22494a.m.cnsza.kvstore.aliyuncs.com:6379/4",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            'TIMEOUT': None,
            "KEY_PREFIX": "cbbweb"
        },
        "second": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://ddf3b048df22494a:PVuser201510@ddf3b048df22494a.m.cnsza.kvstore.aliyuncs.com:6379/5",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            'TIMEOUT': None,
            "KEY_PREFIX": "cbbweb"
        }
    }

    APP_DOMAIN = 'http://127.0.0.1:7777/'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cms_data',
            'USER': 'cbb',
            'PASSWORD': 'abc123!!',
            'HOST': '120.76.78.195',
            'PORT': '3306'
        },
        'cms': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'e4sdb_data',
            'USER': 'chebaba',
            'PASSWORD': 'pvuser201510',
            'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
            'PORT': '3306'
        }
    }

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'verbose': {
                'format': ("%(levelname)s [%(asctime)s] "
                           "%(process)d-%(thread)d "
                           "[%(name)s.%(module)s:%(lineno)s] "
                           "%(message)s"),
                'datefmt': "%Y-%m-%d_%H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
            'sql': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/var/tmp/log/cms/sql.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'runing': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/var/tmp/log/cms/running.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'cms': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/var/tmp/log/cms/cms.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'service': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': '/var/tmp/log/cms/service.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            }
        },
        'loggers': {
            'django.db': {
                'handlers': ['sql'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'django': {
                'handlers': ['runing', 'console'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'cms': {
                'handlers': ['cms', 'console'],
                'level': 'DEBUG',
                'propagate': False
            },
            'service': {
                'handlers': ['service', 'console'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
