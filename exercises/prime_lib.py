import math
def prime(x):
	n = int(math.ceil(math.sqrt(x)))	
	if x == 1:
		return False
				
	for i in range(2 ,n + 1):	
		if x % i == 0 and x != 2: 
			return False					
	
	return True
		