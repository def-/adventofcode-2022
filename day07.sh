#!/bin/sh
rm -rf day07fs
mkdir day07fs
cd day07fs
sed -e "s/^\([0-9]\)/truncate -s \1/" -e "s/^dir /mkdir /" -e "s/\$ ls//" -e "s/$ //" ../day07.in|tail -n +2|sh
echo -n "Part 1: "
find . -type d|while read dir; do (find $dir -type f -printf "%s+"; echo 0)|bc; done|grep -v "[0-9]\{6\}"|paste -s -d+|bc
echo -n "Part 2: "
req_size=$((echo -n "30000000-70000000"; find . -type f -printf "+%s"; echo)|bc)
find . -type d|while read dir; do size=$((find $dir -type f -printf "%s+"; echo 0)|bc); [ $size -ge $req_size ] && echo $size; done|sort -n|head -n1
