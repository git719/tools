#!/bin/bash
# logfilesize
# Tally log file size

# ------ Housekeeping ----------------------
OSTYPE=`uname | tr [A-Z] [a-z]`
DateExt=`date +%Y%M%d`
LogsBasePath=/apps/runtime/apache

# ------ Main ------------------------------
SizeF=/tmp/size.txt
ls -go $LogsBasePath/*/*/logs/*${DateExt} 2>/dev/null | grep -v “ 0 “ | awk ‘{print $3}’ > $SizeF 
TotalBytes=0
For Size in `cat $SizeF` ; do
   (( TotalBytes += Size ))
done

# Commatize for legibility
TotalSize=`echo $TotalBytes |  sed -e :a -e ‘s/\(.*[0-9]\)\([0-9]\{3\}\)/\1,\2/;ta’
exit 0

