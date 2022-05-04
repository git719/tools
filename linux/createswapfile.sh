#!/bin/bash
# createswapfile.sh

read -p "Create and enable a 922MB /var/swapfile on this CentOS host? [y/n] " -n 1 && [[ ! $REPLY =~ ^[Yy]$ ]] && exit 1

dd if=/dev/zero of=/var/swapfile bs=1M count=922 
chmod 600 /var/swapfile
mkswap /var/swapfile 
echo /var/swapfile swap swap defaults 0 0 >> /etc/fstab
swapon -a
echo "You can now vi /etc/fstab, and remove old swap partition, etc."
exit 0
