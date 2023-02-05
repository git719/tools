#!/usr/bin/python
# Capitalize every word in a given file
import sys, os.path
if os.path.exists(sys.argv[1]) :
   print open(sys.argv[1]).read().title()
# Capitalize given string (filename as example)
b = sys.argv[1] ; print b.capitalize()

# BASH/sed version
#sed -e "s/\b\(.\)/\u\1/g" file.txt
