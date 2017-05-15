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

from cbbweb.cms import models

FILE_HEAD = '''# -*- coding: utf-8 -*-

from enum import Enum

# from cbbweb.cms import models

class ModelName(Enum):'''

print(FILE_HEAD)

for model in inspect.getmembers(models, inspect.isclass):
    # print("    " + model[0] + ' = \"' + model[0] + '\"')
    print("    " + model[1]._meta.db_table.upper() + ' = \"' + model[0] + '\"')
    # print("    " + model[1]._meta.db_table + ' = models.' + model[0])
