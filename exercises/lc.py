from sys import argv 
# number and array 
# print numbers from the array that are less than the number


a = 10
b = range(1,15)

def arr(x,y):
	

	return [element for element in y if element < x]

print arr(a,b)