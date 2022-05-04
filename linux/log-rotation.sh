#!/bin/bash
# log-rotation.sh

LOGFILE=/apps/runtime/apache/logs/access.log

# Find oldest log file (highest prefix number)
A=0
for F in `ls -l ${LOGFILE}* | grep "\.[0-9]*$"` ;  do
   NUM=${F##*.}
   (( NUM > A )) && A=$NUM
done

# Rename it as logfilename.<highest+1>, and repeat if necessary
while (( A > 0 )) ; do
   (( B = A + 1 ))
   [[ -f ${LOGFILE}.${A} ]] && mv ${LOGFILE}.${A} ${LOGFILE}.${B}
   (( A = A - 1 ))
done

[[ -f ${LOGFILE} ]] && mv ${LOGFILE} ${LOGFILE}.1

exit 0
