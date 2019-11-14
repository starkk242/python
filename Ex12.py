#Fetching the file name from the user 
print "Enter the file to open"
file1 = raw_input()

#opening the file in the variable txt
txt = open(file1)
print "here's your file" 
#printing the data of the file  
print txt.read()

#Performing similar command
print "Enter the file name again"
filename = raw_input()

txt_again = open(filename)

print txt_again.read()
