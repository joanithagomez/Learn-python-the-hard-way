def cheese_and_crackers(cheese_count, cracker_count):
	print "You have %d cheeses!" % cheese_count
	print "You have %d crackers!" % cracker_count
	print "MAn that's enough for a party"
	print "Get a blanket \n."
	
print "We can just give the function numbers directly:"
cheese_and_crackers(20,30)

print "Or , we can use variables from our script: "
crackers = 10
cheese = 50

cheese_and_crackers(cheese,crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(cheese + 100, crackers + 1000)