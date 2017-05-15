# -*- coding: utf-8 -*-
"""
Django settings for cbbweb project.
"""
import os
from cbbweb.base_settings import BaseConfig


class Prod(BaseConfig):
    DEBUG = False
    ALLOWED_HOSTS = ['*']
    STATIC_URL = '/static/'
    CACHEING = True

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://ddf3b048df22494a:PVuser201510@ddf3b048df22494a.m.cnsza.kvstore.aliyuncs.com:6379/6",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            'TIMEOUT': None,
            "KEY_PREFIX": "cbbweb"
        },
        "second": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://ddf3b048df22494a:PVuser201510@ddf3b048df22494a.m.cnsza.kvstore.aliyuncs.com:6379/7",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            'TIMEOUT': None,
            "KEY_PREFIX": "cbbweb"
        }
    }

    APP_DOMAIN = 'http://www2.chebaba.com/'

    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BaseConfig.BASE_DIR, 'db.sqlite3'),
        # },
        # 'cms': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'e4sdb_data',
        #     'USER': 'chebaba',
        #     'PASSWORD': 'pvuser201510',
        #     'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
        #     'PORT': '3306'
        # }

        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cms_data',
            'USER': 'cms',
            'PASSWORD': 'cms_2016',
            'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
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
                'format': ("%(process)d-%(thread)d [%(asctime)s] "
                           "%(levelname)s [%(name)s:%(lineno)s] %(message)s"),
                'datefmt': "%Y-%m-%d_%H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            }
        },
        'handlers': {
            'sql': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'log/sql.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'runing': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'log/running.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'cms': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'log/cms.log',
                'when': 'MIDNIGHT',
                'backupCount': 30,
                'interval': 1,
                'delay': True,
                'formatter': 'verbose'
            },
            'service': {
                'level': 'DEBUG',
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'filename': 'log/service.log',
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
                'handlers': ['runing'],
                'level': 'DEBUG',
                'propagate': False,
            },
            'cms': {
                'handlers': ['cms'],
                'level': 'DEBUG',
                'propagate': False
            },
            'service': {
                'handlers': ['service'],
                'level': 'DEBUG',
                'propagate': False
            }
        }
    }
