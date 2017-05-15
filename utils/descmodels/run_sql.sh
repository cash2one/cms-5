#!/bin/sh

dateTime=`date +%Y%m%d_%H_%M_%S`
resultFileName="sql/result_"${dateTime}".sql"

python runsql.py "$1" > ${resultFileName}


