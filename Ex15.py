#Creating function with two arguments to be inserted while calling it
def print_two(arg1, arg2):
  print "arg1: %r, arg2: %r" % (arg1, arg2)

#Creating fuction with one argument
def print_one(arg1):
  print "arg1: %r" % arg1
  
#Creating fuction with no argument
def print_none():
  print"I got nothing"

#Calling functions
print_two("Bimal","Singh")
print_one("Bimal")
print_none() 
