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
#Above two lines can be done in one line like : indata = (open(file1)).read()

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
#Above two lines can be done in one line like : (open(file2,'w')).write(indata)

print"Alright Done"

#closing Files
#If using one line on line 13 & 28 then don't write below two lines 
out_file.close()
in_file.close()
