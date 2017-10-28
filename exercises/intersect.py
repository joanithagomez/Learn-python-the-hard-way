from sys import argv 


def intersect(x,y):
	number = []
	for element in x:
		if element in y:
				number.append(element)
	
	return number			
	
	# OR return [element for element in x if element in y]	
	
a = range(1,11)
b = [9, 3, 8, 5,11,20]
				
print intersect(a, b)
		
