# -*- coding: utf-8 -*-
import os
from configurations import Configuration

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

class BaseConfig(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'au940=cqmt3rwu4%49oire=qndb%+dg$e@ksg$1jc4p=(0#av6'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    # CACHE Flag
    CACHEING = False

    # set by chx
    TRAVERSE_CACHE = False
    CHX_DEBUG = False

    ALLOWED_HOSTS = ['*']

    SQL_URL = 'http://e4s.stg.dongfeng-nissan.com.cn/e4s-mp-data/interface/%s/getInfo'
    SMS_URL = 'http://202.96.191.202:8080'
    REDIS_LOCATION = 'REDIS_LOCATION'
    REDIS_REFRESH_LOCATION = 'REDIS_REFRESH_LOCATION'

    # Application definition

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django_jinja',
        'cbbweb.core',
        'cbbweb.cms',
        'cbbweb.site',
        'cbbweb.service',
        'cbbweb.main',
    )

    MIDDLEWARE_CLASSES = (
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

    ROOT_URLCONF = 'cbbweb.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
        {
            'BACKEND': 'django_jinja.backend.Jinja2',
            'APP_DIRS': True,
            'DIRS': [
                'cbbweb/frontend/templates',
                'cbbweb/frontwap/templates',
            ],
            "OPTIONS": {
                "match_extension": ".html",
                "app_dirname": "templates",
                "extensions": [
                    "jinja2.ext.do",
                    "jinja2.ext.loopcontrols",
                    "jinja2.ext.with_",
                    "jinja2.ext.i18n",
                    "jinja2.ext.autoescape",
                    "django_jinja.builtins.extensions.CsrfExtension",
                    "django_jinja.builtins.extensions.CacheExtension",
                    "django_jinja.builtins.extensions.TimezoneExtension",
                    "django_jinja.builtins.extensions.UrlsExtension",
                    "django_jinja.builtins.extensions.StaticFilesExtension",
                    "django_jinja.builtins.extensions.DjangoFiltersExtension",
                ],
                "bytecode_cache": {
                    "name": "default",
                    "backend": "django_jinja.cache.BytecodeCache",
                    "enabled": False,
                },
                "autoescape": True,
                "auto_reload": DEBUG,
                "translation_engine": "django.utils.translation",
            }
        },
    ]

    WSGI_APPLICATION = 'cbbweb.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #     }
    # }

    DATABASE_ROUTERS = ['cbbweb.cms.dbrouter.CmsRouter', 
                        'cbbweb.core.dbrouter.CoreRouter']
    DATABASES = {
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # },
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
            'USER': 'e4sdb_data',
            'PASSWORD': 'e4sdb_data',
            'HOST': '172.26.136.192',
            'PORT': '8065'
        }
    }


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'zh-hans'

    TIME_ZONE = 'Asia/Shanghai'

    USE_I18N = True

    USE_L10N = True

    # USE_TZ = True
    USE_TZ = False

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/
    # STATIC_ROOT = os.path.join(BASE_DIR, 'cbbweb/frontend/static')

    STATIC_ROOT = os.path.join(BASE_DIR, 'static')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "cbbweb/frontend/static"),
        os.path.join(BASE_DIR, "cbbweb/frontwap/static"),
    )

        # LOGGING
        # LOG_SERVER_HOST = ''
        # LOG_SERVER_PORT = ''
        # LOGGING = {
        #     'version': 1,
        #     'disable_existing_loggers': False,
        #     'formatters': {
        #         'verbose': {
        #             'format' : ("%(process)d-%(thread)d [%(asctime)s] "
        #                         "%(levelname)s [%(name)s:%(lineno)s] %(message)s"),
        #             'datefmt' : "%Y-%m-%d_%H:%M:%S"
        #         },
        #         'simple': {
        #             'format': '%(levelname)s %(message)s'
        #         }
        #     },
        #     'handlers': {
        #         'cbbweb_cms_cmstags': {
        #             'level': 'DEBUG',
        #             'class': 'logging.handlers.SocketHandler',
        #             'host': LOG_SERVER_HOST,
        #             'port': LOG_SERVER_PORT,
        #             'formatter': 'verbose'
        #         }
        #     },
        #     'loggers': {
        #         'cbbweb.cms.cmstags': {
        #             'handlers': ['cbbweb_cms_cmstags'],
        #             'level': 'DEBUG',
        #             'propagate': False
        #         }
        #     }
        # }

    # CACHES
    CACHES = {
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'unique-snowflake',
            'TIMEOUT': None
        }
    }

