# -*- coding: utf-8 -*-
"""
Django settings for cbbweb project.
"""
# import os
from cbbweb.base_settings import BaseConfig


class Lc(BaseConfig):
    # ALLOWED_HOSTS = ['']
    
    # DEBUG = False
    DEBUG = True

    CACHEING = False
    # CHX_DEBUG = False
    # TRAVERSE_CACHE = False
    
    # CACHEING = True
    # CHX_DEBUG = True
    # TRAVERSE_CACHE = True

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://:abc123!!@120.76.78.226:6379/4",
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            },
            'TIMEOUT': None,
            "KEY_PREFIX": "cbbweb"
        }
    }

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_jinja',
        # 'debug_toolbar',
        'cbbweb.core',
        'cbbweb.cms',
        'cbbweb.site',
        'cbbweb.service',
        'cbbweb.main',
    )

    MIDDLEWARE_CLASSES = (
        # 'debug_toolbar.middleware.DebugToolbarMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
        'cbbweb.core.middleware.CbbMiddleware',
    )

    # DEBUG_TOOLBAR_PANELS = [
    #     'debug_toolbar.panels.versions.VersionsPanel',
    #     'debug_toolbar.panels.timer.TimerPanel',
    #     'debug_toolbar.panels.settings.SettingsPanel',
    #     'debug_toolbar.panels.headers.HeadersPanel',
    #     'debug_toolbar.panels.request.RequestPanel',
    #     'debug_toolbar.panels.sql.SQLPanel',
    #     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    #     'debug_toolbar.panels.templates.TemplatesPanel',
    #     'debug_toolbar.panels.cache.CachePanel',
    #     'debug_toolbar.panels.signals.SignalsPanel',
    #     'debug_toolbar.panels.logging.LoggingPanel',
    #     'debug_toolbar.panels.redirects.RedirectsPanel',
    # ]

    # INTERNAL_IPS = [
    #     '127.0.0.1',
    #     '192.168.56.1',
    #     '172.26.146.61'
    # ]

    # DEBUG_TOOLBAR_CONFIG = {
    #     'JQUERY_URL' :'//apps.bdimg.com/libs/jquery/2.1.4/jquery.min.js'
    # }

    DATABASE_ROUTERS = ['cbbweb.cms.dbrouter.CmsRouter', 
                        'cbbweb.core.dbrouter.CoreRouter']
    DATABASES = {
        # -------- for test ----------------------
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BaseConfig.BASE_DIR, 'db.sqlite3'),
        # },
        
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cms_data',
            'USER': 'cbb',
            'PASSWORD': 'abc123!!',
            'HOST': '120.76.78.195',
            'PORT': '3306'
        },
        
        # 'cms': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'e4sdb_data',
        #     'USER': 'chebaba',
        #     'PASSWORD': 'pvuser201510',
        #     'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
        #     'PORT': '3306'
        # }

        'cms': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'e4sdb_data',
            'USER': 'root',
            'PASSWORD': '123456',
            'HOST': '127.0.0.1',
            'PORT': '3306'
        }

        # 'cms': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'e4sdb_data',
        #     'USER': 'e4sdb_data',
        #     'PASSWORD': 'e4sdb_data',
        #     'HOST': '172.26.136.192',
        #     'PORT': '8065'
        # }

        # 'cms': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'e4sdb_data',  # 'test_e4s',
        #     'USER': 'dfadmin',
        #     'PASSWORD': 'df_pw_123456',
        #     'HOST': '192.168.56.101',
        #     'PORT': '3306'
        # }

        # --------- for prodution ------------------
        # 'default': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'cms_data',
        #     'USER': 'cms',
        #     'PASSWORD': 'cms_2016',
        #     'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
        #     'PORT': '3306'
        # },
        
        # 'cms': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'e4sdb_data',
        #     'USER': 'chebaba',
        #     'PASSWORD': 'pvuser201510',
        #     'HOST': 'rdsir8k28824m77316sro.mysql.rds.aliyuncs.com',
        #     'PORT': '3306'
        # }
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
