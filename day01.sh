#!/bin/sh
# Part 1
paste -s -d+ day01.in|sed -e"s/++/\n/g"|bc|sort -n|tail -n1
# Part 2
paste -s -d+ day01.in|sed -e"s/++/\n/g"|bc|sort -n|tail -n3|paste -s -d+ -|bc
