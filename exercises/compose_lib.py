def list_sum(list):
	sum = 0	
	
	for index in range(0, len(list)):
		sum = sum + list[index]
		
	return sum
		
print list_sum([1,2,3,4,20])
	