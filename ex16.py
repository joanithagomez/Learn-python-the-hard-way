from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you dont want that , hit CTRL-C (^C). " 
print "If you do want that , hit RETURN." 

raw_input("?")

print "Opening the file..."
target = open(filename,'w')


print "now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: " )
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + '\n'+ line2 + '\n' + line3)

target = open(filename,'r')
print "Reading... "
print target.read()

print "And finally, we close it."
target.close()
