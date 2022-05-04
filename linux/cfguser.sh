#!/bin/bash
# cfguser.sh

[[ "`whoami`" != "root" ]] && printf "\nError. You have to be 'root'.\n\n" && exit 1
[[ "$#" != "1" ]] && printf "\nUsage: ./cfguser.sh <user.pub>\n\n" && exit 1

KEY=$1
USR=${KEY%%.pub}
[[ -n "`id -u $USR 2>/dev/null`" ]] && printf "\nError. User '$USR' already exists.\n\n" && exit 1
[[ "$KEY" != "${USR}.pub" ]] && printf "\nError. Need a key file named $USR.pub!\n\n" && exit 1
DESC=$USR
[[ ! -f "$KEY" ]] && printf "\nError. Missing public key file!\n\n" && exit 1

OSTYPE=`grep -hci ubuntu /etc/*-release | tail -1`
[[ "$OSTYPE" == "0" ]] && OSTYPE=centos || OSTYPE=ubuntu
[[ "$OSTYPE" == "ubuntu" ]] && PWDOPT="-u" || PWDOPT="-fu"

useradd -c "$DESC" -d /home/$USR -m -s /bin/bash $USR
passwd $PWDOPT $USR
[[ ! -d /home/$USR/.ssh ]] && mkdir /home/$USR/.ssh
chmod 700 /home/$USR/.ssh
mv $KEY /home/$USR/.ssh/authorized_keys
chmod 644 /home/$USR/.ssh/authorized_keys
chown -R $USR:$USR /home/$USR
echo ""
find /home/$USR -ls
echo ""
