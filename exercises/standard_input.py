# Usage:
# who | python standard_input.py
# Prints:
#
# Output:
# <output of ls here>
#

import sys


print "Output: " 

# print sys.stdin.read()	

file = sys.stdin

str = file.readline()

while str != "":
	print str.rstrip()
	str = file.readline()
