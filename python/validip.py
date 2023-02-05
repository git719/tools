#!/usr/bin/env python
# validip

import sys

def valid_ip(ip):
    import socket             # Ask socket module if string is a valid IP address
    try:
        socket.inet_aton(ip)  # IP format is correct
        return True
    except socket.error:      # Not correct
        return False

if len(sys.argv[1:]) == 1:
    print(valid_ip(sys.argv[1]))
