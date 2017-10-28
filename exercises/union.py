from sys import argv 


def union(first, second):
	numbers = first[:]

	return first + [element for element in second if element not in first]
	
a = range(1,11)
b = [5,6,7,8,9,20]
				
print union(a, b)



def alternatemethod():	
	numbers = first[:]
		
	for element in second:			
				if not element in first :
					numbers.append(element)
				
	return numbers	