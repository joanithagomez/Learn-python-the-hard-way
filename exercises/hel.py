#if number is not divisible by any number other than 1 and itself 

import sys
n = int(sys.argv[1])

flag = 0
i = 2
while i in range(2, n):
	print "top i value: " , i
 	if n % i != 0:
		flag = 1	
	 	
	i += 1
	
print "flag value: " , flag 

if flag == 1:
	print " %d is prime." % n
else:
 	print " %d is not prime." % n