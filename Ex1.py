cars = 100
space_in_car=4.0
drivers = 30
passangers =90
cars_not_driven = cars - drivers
cars_driven = driven
carpool_capacity = cars_driven * space_in_car
average_passsangers_per_car = passangers/cars_driven

print "there are",cars,"cars availabe"
print"There are only", drivers,"drivers available"
print"There will be ",cars_not_driven,"not driven"
print "We can transport",carpool_capacity,"today" 
print "We have", passangers,"to carpool today"
print "We need to put about",average_passsangers_per_car,"in each car" 
