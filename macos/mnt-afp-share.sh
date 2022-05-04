#!/bin/bash
# mnt-afp-share.sh
NETSHARE=afp://user:pass@idisk.mac.com/user
MOUNTDIR=/Volumes/??
[[ ! -d "$MOUNTDIR" ]] && sudo mkdir -p $MOUNTDIR
sudo mount -t afp $NETSHARE $MOUNTDIR

# Refresh disk arbitration system so Finder gets access privs
disktool -r
exit 0
