#!/bin/zsh

cat input | egrep "(.*[aeiou]){3}" | egrep "(.)\1" | egrep -v "ab|cd|pq|xy" | wc -l

cat input | egrep "(..).*\1" | egrep "(.).\1" | wc -l
