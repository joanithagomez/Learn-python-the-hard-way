the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears','apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:	
	print "This is count %d" % number 
for fruit in fruits:
	print "A fruit of type: %s" % fruit
for i in change:
	print "I got %r" % i
	
elements = []
	
for i in range(0,6):
	elements.append(i)
	print "elements was: %d" % i