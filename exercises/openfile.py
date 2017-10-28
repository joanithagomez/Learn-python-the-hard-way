def option():
	if len(sys.argv) == 1:
		 file = sys.stdin
	else: 
		file = open(sys.argv[1])
