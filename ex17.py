from os.path import exists

from_file=raw_input("enter source filename:")
to_file=raw_input("enter target filename:")

print "Copying from %s to %s"%(from_file,to_file)

#we could do these two on one line too,how?
in_file=open(from_file)
indata=in_file.read()

print "The input file is %d bytes long"%len(indata)

print "Does the output file exist? %r"%exists(to_file)
print "Ready, hit Enter to continue, CTRL-C to abort."
raw_input(">")

out_file=open(to_file,'w')
out_file.write(indata)

print "Alright, all done"

out_file.close()
in_file.close()
