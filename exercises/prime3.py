# Usage:
# python prime3.py 1-10

# Output: [2, 3, 5, 7]



from sys import argv
from prime_lib import prime
	
def convert_to_range(str):
	words = str.split('-')

	num = [int(i) for i in words]

	return range(num[0],num[1]+1)
	
output = []
for element in convert_to_range(argv[1]):
	if prime(element):
		output.append(element)
print output
	

