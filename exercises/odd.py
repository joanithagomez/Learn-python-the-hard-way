# Usage:
# python odd.py 27
# Output: 27 is odd
#
# python odd.py 28
# Output: 28 is not odd
#


def is_odd(n):
	return n % 2 == 0
 
from sys import argv

n = int(argv[1])

if is_odd(n):
	print "%d is even." % n
else:
	print "%d is odd." % n

