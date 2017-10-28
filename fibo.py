print "Fibonacci series!"

def fib(num):
	if num == 1:
		return 0
	elif num == 2:
		return 1
	else:
		return fib(num - 1) + fib(num - 2) 
	
	
for i in [2, 4, 6, 8, 10, 12]:		
	print "%dth fibonacci number is %d" % (i, fib(i))