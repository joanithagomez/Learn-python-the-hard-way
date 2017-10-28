# Usage:
# python prime.py 27
# Output: 27 is not prime
#
# python prime.py 13
# Output: 13 is prime
#

 
import sys

def is_prime(n):
	# if any number between 2 and n can divide n, then return false
	# otherwise return true

	for x in range(2,n):
		if n % x == 0:
			return False

	return True
	
	
def is_prime_old(n):
	flag = 0
	
	for x in range(2,n):
		print "%d mod %d is %d" % (n, x, n % x)
		if n % x != 0:
			print "flag becomes 1"
			flag = 1
		else:
			print "flag becomes 0"
			flag = 0
			
	return (flag == 1)
	


n = int(sys.argv[1])


			
if is_prime(n) and n != 1:
	print "%d is prime" % n
else:
	print "%d is not prime." % n