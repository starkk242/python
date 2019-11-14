print "Ente the file to open"
file1 = raw_input()

txt = open(file1)
print "here's your file" 
print txt.read()

print "Enter the file name again"
filename = raw_input()

txt_again = open(filename)

print txt_again.read()
