#!/usr/bin/env sh

######################################################################
# @author      : mclds (mclds@protonmail.com)
# @file        : file_manipulations
# @created     : Tuesday Apr 26, 2022 18:40:14 WEST
#
# @description : Moves scattered post files to same folder.. 
######################################################################


find /home/mic/python/cli_diary/cli_diary/blog_posts/2021 -type f -exec cp --backup=numbered -t /home/mic/python/cli_diary/cli_diary/blog_posts/collection {} +



