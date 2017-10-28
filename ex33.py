numbers = []

def loop(x,y):
	i = 0


	for x in range(0,11):
		print "At the top i is %d" % i 
		numbers.append(i)

		i = i + y
		print "Numbers now: " , numbers 
		print "At the bottom i is %d" % i
	

loop(2)
print "The numbers:"
for num in numbers:
	print num