#!/bin/bash
# jvmmem
ps auxwww | grep [j]ava | awk '{printf "%-5s%10s%10s   %s\n", $2, $5, $6, $NF}' | sort -k 4
