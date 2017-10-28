# Usage:
# python prime2.py 1,2,3,4

# Output: 
# 1 is not prime
# 2 is prime
# 3 is prime
# 4 is not prime

from sys import argv 
from prime_lib import prime
import math

#['prime2.py', '1,2,3,4'] (string) 

words = argv[1].split(',')
numbers = [int(i) for i in words[0:]]

for element in numbers:

	if prime(element) and element != 1:
		print "%d is prime" % element
	else: 
		print "%d is not prime" % element
		
		