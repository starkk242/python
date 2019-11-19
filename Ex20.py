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