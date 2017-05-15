#!/bin/bash

# sh /project_init.sh

if [ ! $PYTHONHASHSEED ]; then
  echo "export PYTHONHASHSEED=44530219" >> ~/.bash_profile
  source ~/.bash_profile
fi

run_env="Test"
if [ $1 ]; then
    run_env=$1
fi
echo "${run_env} Mode is restarting..."

PID_FILE="/var/tmp/cms.pid"
ACCESS_LOG_FILE="/var/tmp/log/gunicorn/access.log"
ERROR_LOG_FILE="/var/tmp/log/gunicorn/error.log"
LOG_LEVEL="warn"

# svn update
# pip install -r requirements.txt
echo "yes" | ./manage.py collectstatic
kill -9 `cat $PID_FILE`
gunicorn cbbweb.wsgi \
    --env DJANGO_CONFIGURATION=${run_env} \
    --env DJANGO_SETTINGS_MODULE=cbbweb.settings \
    -n cms \
    -w 6 \
    -k gevent \
    -t 30 \
    --backlog 2048 \
    --worker-connections 1000 \
    --keep-alive 2 \
    -p $PID_FILE \
    -b localhost:7777 \
    --error-logfile $ERROR_LOG_FILE \
    --log-level $LOG_LEVEL \
    -D
echo "${run_env} Mode is started..."

#    --max-requests 500 \
#    --access-logfile $ACCESS_LOG_FILE \
#    --graceful-timeout 30 \
#    --threads 20 \

