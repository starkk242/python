the_count = [1,2,3,4,5]
fruits = ['apples','oranges','peras','apricots']
change = [1,'pennies',2,'dimes',3,'quaters']

for number in the_count:
	print "This is Count %d " % number

for fruit in fruits:
	print "A fruit of types: %s " % fruit

for i in change:
	print "I got %r" % i

elements = []

for i in range(0,6):
	print "Adding %d to the list." % i
	elements.append(i)

#print elements[5]

for i in elements:
	print "Elements are: %d" % i 			 