#!/usr/bin/env bash

function rotate() {
    echo 切割文件: $1
    logs_path=$1
    logs_last=`dirname -- ${logs_path}`/`basename -- ${logs_path} | cut -d'.' -f1`/`basename -- ${logs_path}`.$(date -d "yesterday" +"%Y%m%d")
    cp ${logs_path} ${logs_last}
    > ${logs_path}
    rm -f ${logs_path}.$(date -d "7 days ago" +"%Y%m%d")
}

for i in $*
do
    rotate $i
done
