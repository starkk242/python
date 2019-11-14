print "Ente the file to write"
file1 = raw_input()

print "Now going to delete the data of %r" % file1
print "To continue press Enter Else press Ctrl+C"

raw_input('?')

print "Opening the file"
target = open(file1,'w')

print "Getting file ready to edit"
target.truncate()

print "Enter th lines for the data to be inserted "

line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

target.write(line1)
target.write('\n')

target.write(line2)
target.write('\n')

target.write(line3)

print "Done editing closing the file"
target.close()