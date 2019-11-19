print "Let's Practice everything"
print 'You\'d need to know \' bout escapes with \\ that do \n newlines and \t tabes.'

poem = """
\tThe Lovely world 
with logic so firmly planted
cannot discern \n the need of love
nor comprehend passion from intutions
and requires and explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10-2+3-6
print "This shoud be five :%s" % five

def secret_formula(started):
	jelly_beans =started *500
	jars = jelly_beans / 1000
	crate = jars /100
	return jelly_beans,jars,crate

start_point=10000
beans,jars,crate = secret_formula(start_point)

print"with a starting point of %d" %start_point
print "we have %d beans , %d jars, And %d crates" % (beans,jars,crate)

start_point = start_point/10

print "We can also do that this way"
print "We have %d beans, %d jars, %d crate" % secret_formula(start_point)

