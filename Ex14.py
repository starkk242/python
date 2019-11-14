from sys import argv
from os.path import exists

print "Ente the 2 file to copy and pasting"
file1 = raw_input()
file2 = raw_input()

in_file = open(file1)
indata = in_file.read()

print "The input file %d bytes long" % len(indata)

print "Does the output file exist? %r" %exists(file2)
print "Ready,hint Enter to contiue, Ctrl+c to exit"
raw_input()

out_file = open(file2,'w')
out_file.write(indata)

print"Alright Done"

out_file.close()
in_file.close()