
filename = raw_input("File name: ")

# opening file 
txt = open(filename) 

print "Here's your file %r:" % filename  

# call a function on txt named read. 
print txt.read() 
