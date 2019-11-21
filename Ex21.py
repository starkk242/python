import Ex20

sentence = raw_input("enter a line")

words = Ex20.break_words(sentence)
print words

sorte = Ex20.sort_words(words)
print sorte

print Ex20.print_first_word(words)

print Ex20.print_last_word(words)

sort = Ex20.sort_sentence(sentence)
print sort

print Ex20.print_first_and_last(sentence)

print Ex20.print_first_and_last_sorted(sentence)