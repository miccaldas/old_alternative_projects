#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : scrapy_files_pre_clean
# @created     : Wednesday Feb 23, 2022 01:24:30 WET
#
# @description : First clean, still in their original files. 
######################################################################


folders=/home/mic/python/cli_apps/cli_apps/spider_folders/*

for folder in ${folders}; do
    echo "$folder"
    trunc="${folder:50:-7}"
    echo "$trunc"
    results="${folder}/results.txt"

    cp "$results" "${folder}/results1.txt"
    sed -r -i "s/(^\{\x27)description(\x27: \[.*}$)/\1${trunc}\2/g" "${results}"
    sed -ri "s/'//g" "${results}"
    sed -ri "s/ , /, /g" "${results}"
    sed -ri "s/  of,  / of /g" "${results}"
    sed -ri "s/  and,  / and /g" "${results}"
    sed -ri "s/  with,  / with /g" "${results}"
    sed -ri "s/,,/,/g" "${results}"

done
