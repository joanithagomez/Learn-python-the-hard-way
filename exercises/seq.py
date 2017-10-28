# Usage
# python seq.py 10
# produce what seq 10 will produce
# python seq.py 2 10
# produce what seq 2 10 will produce
# python seq.py 1 2 10
# produce what seq 1 2 10 will produce
# python seq.py 10 2
# produce what seq 10 2 will produce

from sys import argv
import sys


num = [int(i) for i in argv[1:]]


def calc(start, end, x):
	for i in range(start, end, x):
		print i

		

	
if len(sys.argv) == 2:
	calc(1, num[0] + 1, 1)
		
				
elif len(sys.argv) == 3:

	if num[0] < num[1]: 
		calc(num[0], num[1] + 1, 1)
		
	elif num[0] > num[1]:
		calc(num[0], num[1] - 1, -1)	
		
				
elif len(sys.argv) == 4:


	mid_num = num[1] 
	
	if num[0] < num[2]:
		calc(num[0], num[2] + 1, mid_num)
		
	elif num[0] > num[2] and mid_num < 0:
		calc(num[0], num[2] - 1, mid_num) 
		
	else: 
		print "Error"
		
		
else: 
	print "usage: seq [-w] [-f format] [-s string] [-t string] [first [incr]] last"						

			
			