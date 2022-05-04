#!/bin/bash
# update-sudoers.sh
# Script updated of /etc/sudoers file (root run from cron)

F1=/etc/sudoers
[[ "`grep -c username $F1`" == "1" ]] && printf "\nTarget user already has sudo access. Aborting.\n\n" && exit 1
F2=/etc/sudoers$$.tmp

cp $F1 $F2

# APPEND below 3 lines
echo "" >> $F2
echo "# Added below via cron'd script `basename $0`" >> $F2
echo "username       ALL = (ALL) NOPASSWD:ALL" >> $F2

# Confirm
visudo -c -f $F2
[[ "$?" -eq "0" ]] && mv $F2 $F1 && chmod 440 $F1
[[ -f "$F2" ]] && echo "Nothing changed. Error running 'visudo -c -f $F2'" && rm -f $F2

exit 0
