#!/usr/bin/env bash

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : change_title
# @created     : Tuesday Apr 26, 2022 19:18:22 WEST
#
# @description : Gets the title of the post and changes to file name. 
######################################################################

collection=/home/mic/python/cli_diary/cli_diary/blog_posts/collection/*

for file in ${collection}; do
    name=$(sed -n -r "s/^.*<p class=\"post-title\">(.*)<\x2fp><\x2fh2>.*$/\1/p1" ${file})
    echo "$name"
    dash=$(echo "$name" | sed -re "s/ /_/g" | tr [:upper:] [:lower:])
    echo "$dash"
    cp -r ${file} new_titles/"$dash".html

done



