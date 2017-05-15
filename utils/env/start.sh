#!/bin/bash
gunicorn cbbweb.wsgi --env DJANGO_CONFIGURATION=Test --env DJANGO_SETTINGS_MODULE=cbbweb.settings -w=5 -b 0.0.0.0:1234 -D



