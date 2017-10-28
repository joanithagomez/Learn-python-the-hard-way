# python histogram.py numbers.txt

# where numbers.txt contains the following:
# 1
# 3
# 5
# 4

# produce this output:

# *
# ***
# *****
# ****

# make this program also accept standard input


from sys import argv
import sys


if len(sys.argv) == 1:
	file = sys.stdin 
else:
	file = open(argv[1])
	
for i in file:
	print '*' * int(i)