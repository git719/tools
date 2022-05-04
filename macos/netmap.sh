#!/bin/bash
# netmap.sh
# Toggles home share mounting 

SHARE="winServer.mydomain.com/myshare"
SHAREDIR="/Volumes/SharePath"
NETHOME="$SHAREDIR/Home/user1"

printf "\nNETWORK : afp://$SHARE/Home/user1\n"
printf "LOCAL   : $NETHOME\n"

if [[ -d "$NETHOME" ]]; then
   umount $SHAREDIR;
else
   mkdir $SHAREDIR
   read -s -p "Net PWD?: " PWD
   mount_afp afp://user1:$PWD@$SHARE $SHAREDIR
   printf "\n"
fi

if [[ -d "$NETHOME" ]]; then
   printf "STATUS  : ON (mapped)\n\n"
else
   printf "STATUS  : OFF (unmapped)\n\n"
fi

exit 0
