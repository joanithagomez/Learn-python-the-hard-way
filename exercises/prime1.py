# Usage:
# python prime1.py 1 2 3 4
#
# Output: 
# 1 is not prime
# 2 is prime
# 3 is prime
# 4 is not prime




from sys import argv 
import math
from prime_lib import prime
		
numbers = [int(i) for i in argv[1:]]


for element in numbers:
	if prime(element):
		print "%d is prime" % element
	else: 
		print "%d is not prime" % element






	
