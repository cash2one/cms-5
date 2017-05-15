#!/bin/sh

cur_pwd=`pwd`

cd ../..

python manage.py inspectdb --configuration=Dev --database cms > models.py

mv -f models.py $cur_pwd
cd $cur_pwd

awk 'BEGIN{isinclude=0; print "--------------------" } \
{if( ($0 ~ /is a guess/) || ($0 ~ /Field renamed/) || ($0 ~ /unique_together/) ) {print FILENAME ":" NR "\t|" $0; isinclude=1}} \
END{if(isinclude == 1) {print "===== " FILENAME " =====\n"}}' models.py

