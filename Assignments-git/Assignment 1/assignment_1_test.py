# COMP9021 Assignment 1
# Christopher Lam

# NOTES:
# Think about differences in using 'in', 'is', '=='
# Maybe dont use 2. THe problem with 2 is that we have to figure out the number of solutions given several 2s


import os
import re

# -------------------------------------------------------------- punctuation_split fn ------------------------------------------------------------
# DOUBLE TEST punctuation_split
	# Especially regex part and think about special case displays of mix of letters and punctuation to create words
# NOTE!!! WHAT ABOUT EDGE CASE OF WORD ENDING WITH '
# MAKE SURE I ACCOUNT FOR THAT

# str.replace --> all \n with ' ' (Also, what about \t, others with \) <-- \t should equate to ' ' so should be fine
# str.replace --> all punctuation with . (assuming ? and . have same meaning)

def punctionation_split (file, text):
	for line in file: # Each line in in iterator is just a str
		line = line.replace('?', '.') # <----------------- NOTE this is only ok if '?' has no special difference in speech comprehension
		line = line.replace('!', '.')
		line = line.replace('\n', ' ')
		line = line.replace(',', ' ') # <----------------- NOTE this is only ok if ',' has no special difference in speech comprehension 
		print(line)
		line_list = line.split(' ')
		print(line_list)
		for word in line_list:
			split = re.search('([\"\'.?!,]*)([a-zA-Z\']*)([\"\'.?!,]*)', word) # word potentially surrounded by punctuation on either side
			word_split = split.groups()
			for split_word in word_split:
				text.append(split_word)
	while True: # Removing extra '' in list created by * in regex
		try:
			text.remove('')
		except:
			break

# -------------------------------------------------------------- find_sirs fn ------------------------------------------------------------
# Used to find all sirs, also useful for finding sirs in speech
	# Not sure if speech sir search is same implementation though
# Right now, all it does is return the list of sirs

def find_sirs (text, list_of_sirs):
	word_pos = 0
	while word_pos != len(text): # Allows situational double jumps
		if text[word_pos] == 'Sir':
			if text[word_pos + 1] not in list_of_sirs:
				list_of_sirs.append(text[word_pos + 1])
		elif text[word_pos] == 'Sirs':
			while text[word_pos + 1] != 'and':
				if text[word_pos + 1] not in list_of_sirs:
					list_of_sirs.append(text[word_pos + 1])
				word_pos += 1
			word_pos += 1
			if text[word_pos + 1] not in list_of_sirs:
				list_of_sirs.append(text[word_pos + 1])
		word_pos += 1
	return sorted(list_of_sirs)

# -------------------------------------------------------------- speech_processor fn ------------------------------------------------------------
# Used to find all sirs, also useful for finding sirs in speech

def speech_processor (text, dictionary):
	pass

# -------------------------------------------------------------- truth_processor fn ------------------------------------------------------------
# Used to find all sirs, also useful for finding sirs in speech

def truth_processor (dictionary_of_statements):
	pass

# ------------------------------------------------------------------- CODE BODY -----------------------------------------------------------------

text = ['.'] # dont have to adjust parsing or sentence checking. Can also remove later
list_of_sirs = [] # Since lists are ordered, I prefer to use lists. Just check for duplication before adding an element
dictionary_of_statements = {}
solutions_list = []

file_name = input('Which text file do you want to use for the puzzle? ')
with open('test_1.txt') as file:

	# return a list of words and punctuation in text
	punctionation_split(file, text)

	print()
	print(text)
	print()
	print(' '.join(text))
	print()

	# find all sirs in a sorted list
	find_sirs(text, list_of_sirs)


	# Iterating through list of words in string
	# Store sentence start '.'
		# NOTE: I think remove the '.' initialisation in text
		# sentence_start = 0 would do the same thing and we really only need to keep track of sentence endings '.'

	# Iterate, if " found ,then it is a speech sentence
	# Iterate until end found
	# Once end found,
	# Pass start and end into a function to determine statement type
		# Within this statement, also pass through find_sirs to find sirs mentioned
		# DOUBLE CHECK ASSUMPTION THAT ONLY 1 statement type can be in a statement
		# Also, that only 1 can be in statement (i.e. cant say 'Sir Jack is a Knight and Sir Jill is a Knave')
	# This function would then append a list of tuples to dictionary of lists
	speech_processor(text, dictionary_of_statements)

	# Lastly, a truth processing function
	# Given dictionary of list of tuples, find all matching statements
	# Matching statements determine solution
	truth_processor(dictionary_of_statements)

	# Printing who the sirs are here
	print('The Sirs are: ', end = '')
	for name in range(len(list_of_sirs)):
		if name != len(list_of_sirs) - 1:
			print(list_of_sirs[name], end = ' ')
		else:
			print(list_of_sirs[name])

	# Printing the solutions here
	if len(solutions_list) == 0:
		print('There is no solution.')
	elif len(solutions_list) > 1:
		print('There are', len(solutions_list), 'solutions.')
	else:
		print('There is a unique solution:')
		for sir in len(solutions_list):
			if solutions_list[sir] == 0:
				print('Sir', list_of_sirs[sir], 'is a Knave.')
			else:
				print('Sir', list_of_sirs[sir], 'is a Knight.')
# ----------------------------------------------------------------------------------------------------------------------------------------------







