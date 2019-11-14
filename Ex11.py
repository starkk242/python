#similar to Ex10.py
from sys import argv
script , user_name = argv
prompt = '> '

print "Hi %s I'm the%s script" % (user_name,script)
likes = raw_input(prompt)
