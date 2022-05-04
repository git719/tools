#!/bin/bash
# isomake

IMG=image.iso

[[ -z "$1" ]] && printf "\nUSAGE: `basename $0` <DIR>\n\n" && exit 1

printf "\nEdit me ($0) to select which image to create.\n\n" ;  exit 1

# Create bootable SOE DSP image (works)
#printf "\nmkisofs -o $IMG -J -R -relaxed-filenames -no-iso-translate -input-charset cp437 -b apps/boot.ima -c apps/boot.cat $1\n\n"
#mkisofs -o $IMG -J -R -relaxed-filenames -no-iso-translate -input-charset cp437 -b apps/boot.ima -c apps/boot.cat $1

# Create Windows readable image (works)
#printf "\nmkisofs -o $IMG -J -R -relaxed-filenames -no-iso-translate $1\n\n"
#mkisofs -o $IMG -J -R -relaxed-filenames -no-iso-translate $1

# Create bootable ISOLINUX image (needs testing)
printf "\nmkisofs -o $IMG -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table $1\n\n"
mkisofs -o $IMG -b isolinux/isolinux.bin -c isolinux/boot.cat -no-emul-boot -boot-load-size 4 -boot-info-table $1
