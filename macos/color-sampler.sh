#!/bin/bash
# color-sampler.sh

# Escape sequence: Simplest method but sometimes can interfere with other programs
GRAY2='\e[1;30m'   RED='\e[0;31m'     RED2='\e[1;31m'
GREEN='\e[0;32m'  GREEN2='\e[1;32m'  YELLOW='\e[0;33m'  YELLOW2='\e[1;33m'
BLUE='\e[0;34m'   BLUE2='\e[1;34m'   PURPLE='\e[0;35m'  PURPLE2='\e[1;35m'
CYAN='\e[0;36m'   CYAN2='\e[1;36m'   GRAY='\e[0;37m'    WHITE='\e[1;37m'
NC='\e[0m'

Sample="${GREEN}2total 8
drwx------+  3 lcapella  staff    96 Mar  9  2017 Movies
drwx------@  5 lcapella  staff   160 Mar 10  2017 Applications
drwxr-xr-x+  6 lcapella  staff   192 Mar 10  2017 Public${NC}"

printf "${GRAY2}\$ ${NC}\n"
printf "$Sample\n"
printf "${GRAY}\$ ${NC}\n"
printf "$Sample\n"
printf "${RED}\$ ${NC}\n"
printf "$Sample\n"
printf "${RED2}\$ ${NC}\n"
printf "$Sample\n"
printf "${GREEN2}\$ ${NC}\n"
printf "$Sample\n"
printf "${GREEN}\$ ${NC}\n"
printf "$Sample\n"

printf "${YELLOW}\$ ${NC}\n"
printf "$Sample\n"
printf "${YELLOW2}\$ ${NC}\n"
printf "$Sample\n"
printf "${BLUE}\$ ${NC}\n"
printf "$Sample\n"
printf "${BLUE2}\$ ${NC}\n"
printf "$Sample\n"
printf "${PURPLE}\$ ${NC}\n"
printf "$Sample\n"
printf "${PURPLE2}\$ ${NC}\n"
printf "$Sample\n"

printf "${CYAN}\$ ${NC}\n"
printf "$Sample\n"
printf "${CYAN2}\$ ${NC}\n"
printf "$Sample\n"
printf "${WHITE}\$ ${NC}\n"
printf "$Sample\n"
