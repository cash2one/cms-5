#!/bin/bash
if [ ! -d "/var/tmp/log/gunicorn" ]; then
  echo "mkdir -p /var/tmp/log/gunicorn for gunicorn"
    mkdir -p /var/tmp/log/gunicorn
fi

if [ ! -d "/var/tmp/log/cms" ]; then
    echo "mkdir -p /var/tmp/log/cms for project"
    mkdir -p /var/tmp/log/cms
    echo "project init done."
fi
