# print lines of input (standard or file)
from sys import argv
import sys 

	if len(sys.argv) == 1:
		 file = sys.stdin
	else: 
		file = open(sys.argv[1])


def word_count(in_file):
	count = 0
	for line in in_file:	
		if line != '':
			count += 1 
	return count
	
print word_count(file)