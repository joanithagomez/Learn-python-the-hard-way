# input here means either standard input or a file passed as argument

# Part 1

# python filter.py odd
# prints only odd numbers in input

# python filter.py even
# prints only even numbers in input

# python filter.py prime
# prints only prime numbers in input
 
# part 2
# python filter.py >100
# prints only numbers > 100 in input
# the "100" should be variable
# Eg: I should be able to use >50

# python filter.py <100
# prints only numbers > 100 in input
# the "100" should be variable
# Eg: I should be able to use >50

# part 3
# learn about lambdas in python, and replace odd/even etc with lambda functions

from sys import argv
import sys
import math
from prime_lib import prime

 		
if len(sys.argv) == 2:
	file = sys.stdin	 	 
else:      					
	file = open(argv[2])


def input_read(in_file):
	return [int(x) for x in in_file]


def filter(in_file, condition):
	 for i in in_file:
	 	if condition(i):
	 		print i

def even(n):
	return n % 2 == 0	
	
def even_filter(in_file):
	filter(in_file, even)
 		
def odd(n):
	return n % 2 != 0
	
def odd_filter(in_file):
	filter(in_file, odd)
 			
 	
def prime_filter(in_file):
	filter(in_file, prime)

# print numbers greater than 100 

def make_comparer(compare, input):
	def comparenum(a):
		# a > input
		# a < input
		
		if compare(a, input):
			return True
		else:
			return False
	return comparenum
	

def greater_filter(num, infile):
	def greater(a, input):
	
		return a > input
		
	filter(infile, make_comparer(greater, num))
	
def lesser_filter(num, infile):
	def lesser(a, input):
	
		return a < input
		
	filter(infile, make_comparer(lesser, num))


			
if argv[1] == 'odd':
	odd_filter(input_read(file))
	
elif argv[1] == 'even':
	even_filter(input_read(file))	
	
elif argv[1] == 'prime':
	prime_filter(input_read(file))
	
elif '>' in argv[1]:
	num = argv[1].split('>')
	number = int(num[1])
	greater_filter(number, input_read(file))
#	print [i for i in input_read(file) if i > number]
	
		
elif '<' in argv[1]:
	num = argv[1].split('<')
	number = int(num[1])
	lesser_filter(number, input_read(file))
#	print [i for i in input_read(file) if i < number]
	
else:
	print "Error"
	


