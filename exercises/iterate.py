# print_list(list) -> prints every element in the list
# print_double_list(list) -> prints the double of every element in the list
from __future__ import print_function

from prime_lib import prime

list = [1,2,3,4,6,7,8,9]

def iterate(list, fun):
	for i in list:
		fun(i)


def map_list(list, fun):
  # return a new list composed of every element in list passed through fun
  list2 = []
  for i in list:
  	list2.append(fun(i))
  
  return list2

print(map_list([1,2,3], lambda x: x * 2))
  
# Eg:
# map_list([1, 2, 3], lambda x: x*2)
# should return [2, 4, 6]  
# map_list([1, 2, 3], lambda x: x+1)
# should return [2, 3, 4]  

def print_double_list(list):
	
	iterate(list,lambda i: print(i*2))

#print_double_list(list)

print([ "Hello " + x for x in ["Jo","Jonah"]])

def filter_list(list, fun):
	# return a new list, composed of elements in list which return True when passed through fun
	list2 = []
	for i in list: 
		if fun(i):
			list2.append(i)
	return list2

print(filter(lambda x: x % 2 == 0,[1, 2, 3, 4]))

#Use filter to check following conditions:
# - odd numbers


print(filter(lambda x: x % 2 != 0,list))

	
# - prime numbers

print(filter(prime,list))

# - multiples of 7

print(filter(lambda x: x % 7 == 0, list))



# - greater than 5

print(filter(lambda x: x > 5,list))

# - greater than n

a = lambda x: lambda y: y > x

print(filter(a(7),list))

#print(filter(lambda x: x > n, list))

#Eg:
#(filter_list([1, 2, 3, 4], lambda x: x % 2 == 0))
# returns [2, 4]
