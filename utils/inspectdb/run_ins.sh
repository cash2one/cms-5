#!/bin/sh

python inspectdb.py > models.py

awk 'BEGIN{isinclude=0; print "--------------------" } \
{if( ($0 ~ /is a guess/) || ($0 ~ /Field renamed/) || ($0 ~ /unique_together/) ) {print FILENAME ":" NR "\t|" $0; isinclude=1}} \
END{if(isinclude == 1) {print "===== " FILENAME " =====\n"}}' models.py

