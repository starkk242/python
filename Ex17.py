#from sys import argv
#script, input_file = argv

print "Enter the file name"
input_file=raw_input()

def print_all(f):
    print f.read()
    
def rewind(f):
    f.seek(0)
        
def print_a_line(line_count, f)
    print line_count, f.readline()
   
current_file = open(input_file)  

print "First let's print the whole file:\n"

print_all(current_file)

print "Now lets rewind it"

rewind(current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file) 