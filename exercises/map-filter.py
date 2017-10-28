"""Write a program which can map() and filter() to make a list whose elements are the squares of even numbers in 
[1,2,3,4,5,6,7,8,9,10]. Look up the documentation of map and filter, if you don't remember. Try changing it to 
print the squares of odd numbers instead. Use lambdas where you can.
"""

from sys import argv
import sys

if len(sys.argv) == 1:
	file = sys.stdin 
else: 
	file = open(sys.argv[1])
	

filter(