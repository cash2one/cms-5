#!/usr/bin/env python

# -*- coding: utf-8 -*-


import sys
import os
import inspect

import django


sys.path.append('../..')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cbbweb.settings")
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

import configurations
configurations.setup()

from cbbweb.core.utils import service

IGNORE_FUNC = [
    'redis_func',
]

FILE_HEAD = '''# -*- coding: utf-8 -*-

from enum import Enum

# from cbbweb.core.utils import service

class ServiceName(Enum):'''

print(FILE_HEAD)

for func in inspect.getmembers(service, inspect.isfunction):
    if func[0] not in IGNORE_FUNC:
        # print("    " + func[0] + ' = service.' + func[0])
        print("    " + func[0] + ' = \"' + func[0] + '\"')
