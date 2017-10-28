# Usage python prime4.py numbers.txt
# Prints out just the prime numbers in numbers.txt
# optionally, if no argument is passed, read standard input

from sys import argv
import sys
import math
from prime_lib import prime

if len(sys.argv) == 1:
	current_file = sys.stdin 
else: 
	filename = sys.argv[1]
	current_file = open(filename) 


def list_read(file):
	return [int(x) for x in file]

def list_read1(file):
	str = file.readline()
	list = []
	while str != "":
		list.append(int(str))
		str = file.readline()
	
	return list
	
for i in list_read(current_file):
	prime(i)
	if prime(i): 
		print i


current_file.close()

