people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the car"
elif cars < people:
	print " We shiould not take the car"
else:
	print "We can't decide" 

if buses > cars:
	print "That's too many buses"
elif buses < cars:
	print "Maybe we should take buses"
else :
	print "We still can't decide"

if people > buses:
	print "Alriught let's just take the bus"
else:
	print "Fine let's stay home"