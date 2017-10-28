# f = lambda x: x + 1
# g = lambda y: y + 2
# compose([f, g]) -> return a function (or lambda) which is the composition of f and g
# compose([f, g])(10) - returns 13

def compose():
	
	a = lambda x +1 : lambda g: g + 2
	return a 
print compose()(10)(2)
