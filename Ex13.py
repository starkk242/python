#Similar to Ex12.py
#Writing the data in the file  
print "Ente the file to write"
file1 = raw_input()

print "Now going to delete the data of %r" % file1
print "To continue press Enter Else press Ctrl+C"

raw_input('?')

print "Opening the file"
#Opening the file in var target in write mode
target = open(file1,'w')

print "Getting file ready to edit"
#Removing the file from the file
target.truncate()

print "Enter th lines for the data to be inserted "

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

#Writing the new data in the file
target.write(line1)
target.write('\n')

target.write(line2)
target.write('\n')

target.write(line3)

print "Done editing closing the file"
target.close()
