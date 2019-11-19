def break_words(stuff):
	"""this function will break upwords for us"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""Prints the first word after popping it of"""
	word = words.pop(0)
	return word

def print_last_word(words):
	"""Prints the last word"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in the full sentence and return the sorted words"""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""print the first and last words of the sentence"""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the word then print the first and last one"""
	word = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)
	
	
'''
#Way to execute this program is to import the program in, another program this is kind of an include file
>>> import ex25
 >>> sentence = "All good things come to those who wait."
 >>> words = ex25.break_words(sentence)
 >>> words
 ['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
 >>> sorted_words = ex25.sort_words(words)
 >>> sorted_words
 ['All', 'come', 'good', 'things', 'those', 'to', 'wait.', 'who']
 >>> ex25.print_first_word(words)
 All
 >>> ex25.print_last_word(words)
 wait.
 >>> wrods
 Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 NameError: name 'wrods' is not defined
 >>> words
 ['good', 'things', 'come', 'to', 'those', 'who']
 >>> ex25.print_first_word(sorted_words)
 All
 >>> ex25.print_last_word(sorted_words)
 who
 >>> sorted_words
'''
