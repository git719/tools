#!/bin/bash 
# admingrp.sh

SUDOFILE=/etc/sudoers
if [[ -z "`chmod 640 $SUDOFILE`" ]]; then
   if [[ -z "`grep '%admin' $SUDOFILE`" ]]; then
      cp $SUDOFILE $SUDOFILE.$$.bak && chmod 400 $SUDOFILE.$$.bak
      cat >> $SUDOFILE <<End-of-message

## Allows people in group admin to run all commands
%admin  ALL=(ALL)       ALL
End-of-message
      if [[ -z "`grep '^admin:' /etc/group`" ]]; then
         groupadd admin 
      fi
   else
      echo "%dmin already in $SUDOFILE"
   fi
   chmod 440 $SUDOFILE
else
   echo "Error. Unable to make changes to file $SUDOFILE"
fi

exit 0
