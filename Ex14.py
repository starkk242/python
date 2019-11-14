#importing files
from sys import argv
from os.path import exists

#Fetching file names from the user  
print "Ente the 2 file to copy and pasting"
file1 = raw_input()
file2 = raw_input()

#Opening file and saving the data of the file in a variable 
in_file = open(file1)
indata = in_file.read()

#Printing file length 
print "The input file %d bytes long" % len(indata)

#The command exists will give true if file exists or vice versa  
print "Does the output file exist? %r" %exists(file2)

#Consent of the user
print "Ready,hint Enter to contiue, Ctrl+c to exit"
raw_input()

#opening second file in wirte mode and writing data in the second file 
out_file = open(file2,'w')
out_file.write(indata)

print"Alright Done"

#closing Files
out_file.close()
in_file.close()
