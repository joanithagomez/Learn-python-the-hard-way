from sys import argv ; from os.path import exists;script, fromfile , tofile = argv;

print " Input file is %d bytes long. " % len(indata)

print "does the output file exist? %r " % exists(tofile)

out_file = open(tofile,'w')
out_file.write(indata)

out_file.close()
in_file.close()
