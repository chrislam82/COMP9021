# COMP9021 Assignment 1
# Christopher Lam

# NOTES:
# Think about differences in using 'in', 'is', '=='
# Maybe dont use 2. THe problem with 2 is that we have to figure out the number of solutions given several 2s


import os
import re

# -------------------------------------------------------------- text_split fn ------------------------------------------------------------
# DOUBLE TEST punctuation_split
	# Especially regex part and think about special case displays of mix of letters and punctuation to create words
# NOTE!!! WHAT ABOUT EDGE CASE OF WORD ENDING WITH '
# MAKE SURE I ACCOUNT FOR THAT

# str.replace --> all \n with ' ' (Also, what about \t, others with \) <-- \t should equate to ' ' so should be fine
# str.replace --> all punctuation with . (assuming ? and . have same meaning)

# NOTE, here for .groups, i think I can just do list(split.groups())
	# Save a few lines of code


def text_split (file, text):
	for line in file: # Each line in in iterator is just a str
		line = line.replace('?', '.') # <----------------- NOTE this is only ok if '?' has no special difference in speech comprehension
		line = line.replace('!', '.')
		line = line.replace('\n', ' ')
		line = line.replace(',', ' ') # <----------------- NOTE this is only ok if ',' has no special difference in speech comprehension 
		print(line)
		line_list = line.split(' ')
		print(line_list)
		for word in line_list:
			split = re.search('([\"\'.?!,:]*)([a-zA-Z\']*)([\"\'.?!,:]*)', word) # word potentially surrounded by punctuation on either side
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

# -------------------------------------------------------------- process_speech fn ------------------------------------------------------------
# Within this statement, also pass through find_sirs to find sirs mentioned
# DOUBLE CHECK ASSUMPTION THAT ONLY 1 statement type can be in a statement
# Also, that only 1 can be in statement (i.e. cant say 'Sir Jack is a Knight and Sir Jill is a Knave')
# This function would then append a list of tuples to dictionary of statements

# yep so for 2, if somebody isnt mentioned, i have to repeat the function and create a separate entity 
# Question is, how to implement for multiple 2s?
# Would that work?

def process_speech (text, list_of_sirs, dictionary_of_statements):

	start = 0
	pass

	# So store statuses in a list of lists where each 
	# prduct(*list()) # to multiply a all tuples in a list of arbitrary length

	# Iterating through list of words in string
	# Store sentence start '.'
		# NOTE: I think remove the '.' initialisation in text
		# sentence_start = 0 would do the same thing and we really only need to keep track of sentence endings '.'

	# Iterate, if " found ,then it is a speech sentence
	# Iterate until end found
	# Once end found,

# -------------------------------------------------------------- find_solutions fn ------------------------------------------------------------
# Find all solutions by processing dictionary_of_statements 
	# We need to test if each solution for one person matches a solution from other sirs
	# If not, then we have conflicting statements, something one person said cant be a truth; they are speaking gibberish
	# If only one person spoke, in which case their statements is the solutions

def find_solutions (list_of_sirs, dictionary_of_statements, solutions_list):
	if not dictionary_of_statements: # Nobody spoke, so return none, ending function
		return

	sirs_who_spoke = list(dictionary_of_statements.keys())
	first_sir, rest_of_sirs = sirs_who_spoke[0], sirs_who_spoke[1:] # Only need to check statements from first sir vs the rest

	# This code is for if someone spoke
	for truth in range(0,2): # Checking Knave Tuples then Knight Tuples
		for solution in dictionary_of_statements[first_sir][truth]:
			if rest_of_sirs == []: # Nobody else spoke
				solutions_list.append(solution) # If nobody else spoke, all solutions are valid
			for other_sirs in rest_of_sirs: # So I skip the first person since that is themself
				if solution in dictionary_of_statements[other_sirs][0]:
					continue # to the next sir
				elif solution in dictionary_of_statements[other_sirs][1]:
					continue # So if a solution (tuple) is found within list of tuples for another person, then it is potentially valid solution
				else:
					break # Will go to next solution, so the solution skipped is not valid
			solutions_list.append(solution) # Solution has been found in all sirs
	# If no solution
		# So later, if nobody spoke, then final answer solutions = 2**(number of sirs)
		# If somebody spoke, then final answer is no solution

# --------------- TESTING FOR ABOVE ---------------
# Question to solve:
# Can I have solutions stated by 2 different people which dont match but are both true
# I.e. John states something potentailly true
# Jack states something potentially True
# But they arent the same and they dont conflict?
# Most likely not, but need to prove

# If my hunch is correct, then I can use if tuple in next, for just one person, since if the statements by another person arent in the first person, they are automatically false

# AND OTHER TESTING I CAN THINK OF...

# ------------------------------------------------------------------- CODE BODY -----------------------------------------------------------------

text = ['.'] # dont have to adjust parsing or sentence checking. Can also remove later
list_of_sirs = [] # Since lists are ordered, I prefer to use lists. Just check for duplication before adding an element
dictionary_of_statements = {} # Need to store names # Actually dont need to store true or false assumptions. That will match pos of name in tuple
solutions_list = []

file_name = input('Which text file do you want to use for the puzzle? ')
with open('test_1.txt') as file:

	print ('....................................................')
	# return a list of words and punctuation in text
	text_split(file, text)

	print ('....................................................')
	print()
	print(text)
	print()
	print(' '.join(text))
	print()
	print ('....................................................')

	# find all sirs in a sorted list
	find_sirs(text, list_of_sirs)

	# Fill dictionary_of_statements
	process_speech(text, list_of_sirs, dictionary_of_statements)

	# Find solutions given someone spoke
	find_solutions(list_of_sirs, dictionary_of_statements, solutions_list)

	# Printing who the sirs are here
	print('The Sirs are: ', end = '')
	for name in range(len(list_of_sirs)):
		if name != len(list_of_sirs) - 1:
			print(list_of_sirs[name], end = ' ')
		else:
			print(list_of_sirs[name])

	# Printing the solutions here
		# NOTE: HAVNT CONTROLLED FOR CONFLICTING STATEMENTS --> NO SOLUTION and THERE MIGHT BE SOMETHING ELSE I HAVNT CONTROLLED FOR BUT I CANT REMEMBER
	if len(solutions_list) == 0:
		print('There is no solution.')
	elif len(solutions_list) > 1:
		print('There are', len(solutions_list), 'solutions.')
	else:
		print('There is a unique solution:')
		for sir in len(solutions_list):
			if solutions_list[sir] == 0:#<------ Note I believe this is wrong, it is a list with a tuple inside, so need to access twice to get elements of tuple
				print('Sir', list_of_sirs[sir], 'is a Knave.')
			else:
				print('Sir', list_of_sirs[sir], 'is a Knight.')
# ----------------------------------------------------------------------------------------------------------------------------------------------







