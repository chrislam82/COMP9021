# COMP9021 Assignment 1
# Christopher Lam
# Not the prettiest...

# NOTES:
# Think about differences in using 'in', 'is', '=='

import os
import re

# -------------------------------------------------------------- text_split fn ------------------------------------------------------------
# DOUBLE TEST text_split
# str.replace --> all \n with ' ' (Also, what about \t, others with \) <-- \t should equate to ' ' so should be fine

def text_split (file, text):
	for line in file: # Each line in in iterator is just a str
		line = line.replace('?', '.') # <----------------- NOTE this is only ok if '?' has no special difference in speech comprehension
		line = line.replace('!', '.')
		line = line.replace('\n', ' ')
		line = line.replace(',', ' ') # <----------------- NOTE this is only ok if ',' has no special difference in speech comprehension and if 2 forms cant exist
		print(line)
		line_list = line.split(' ')
		print(line_list)
		for word in line_list:
			split = re.search('([\"\'.?!,:]*)([a-zA-Z]*)([\"\'.?!,:]*)', word) # word potentially surrounded by punctuation on either side
			text += list(split.groups())
	while True: # Removing extra '' in list created by * in regex
		try:
			text.remove('')
		except:
			break

# -------------------------------------------------------------- find_sirs fn ------------------------------------------------------------
# Used to find all sirs, also useful for finding sirs in speech
	# Not sure if speech sir search is same implementation though

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
	return sorted(list_of_sirs) 				# <---------------- Fix this

# -------------------------------------------------------------- process_speech fn ------------------------------------------------------------
# Given text, find sentences, process, then pass into process_claims to fill dictionary_of_claims
def process_speech (text, list_of_sirs, dictionary_of_claims):
	speech_found = False
	start_of_sentence = 0
	end_of_sentence = 0
	who_spoke = None
	who_is_mentioned = []

	for word_pos in range(len(text)):
		if '\"' in text[word_pos]: # Found a sentence that has speech
			if speech_found == False:
				start_of_speech = word_pos # Storing where speech starts in sentence
			else:
				end_of_speech = word_pos # Storing where speech ends in sentence
			speech_found = True # Set Boolean to True
		if '.' in text[word_pos]:
			end_of_sentence = word_pos
			if speech_found == True:
				who_spoke = find_who_spoke(text, start_of_sentence, end_of_sentence, start_of_speech, end_of_speech)
				who_is_mentioned, type_of_statement, type_of_claim = find_what_is_mentioned(text, list_of_sirs, who_spoke, who_is_mentioned, start_of_speech, end_of_speech)
				process_claim(list_of_sirs, dictionary_of_claims, who_is_mentioned, type_of_statement, type_of_claim)
			start_of_sentence, speech_found = end_of_sentence, False # resetting

# -------------------------------------------------------------- sub fns for process_speech fn ------------------------------------------------------------
def find_who_spoke (text, start_of_sentence, end_of_sentence, start_of_speech, end_of_speech):
	while start_of_sentence < end_of_sentence:
		if start_of_sentence < start_of_speech or start_of_sentence > end_of_speech:
			if 'Sir' in word:
				who_spoke = text[start_of_sentence + 1]
				break
	return who_spoke

def find_what_is_mentioned (text, list_of_sirs, who_spoke, who_is_mentioned, start_of_speech, end_of_speech):
	# Finds:
		# Whos is mentioned
		# status_claim: Knight(1) or Knave(0)
		# type_of_statement:
			# 1 --> At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
			# 2 --> At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
			# 3 --> Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
			# 4 --> All/all of us are Knights/Knaves
			# 5 --> I am a Knight/Knave
			# 6 --> Sir Sir_Name is a Knight/Knave
			# 7 --> Disjunction_of_Sirs is a Knight/Knave
			# 8 --> Conjunction_of_Sirs are Knights/Knaves

	word_pos = 0
	while word_pos != len(text[start_of_speech:end_of_speech]):
		# Finding who is mentioned
		if text[word_pos] == 'I': # Since technically 'I' can be a name --> 'Sir I'
			if text[word_pos - 1] == 'and' or [word_pos + 1] == 'am'or [word_pos + 1] == 'or':
				who_is_mentioned.append(who_spoke)
		if text[word_pos] == 'Sir':
			if text[word_pos + 1] not in who_is_mentioned:
				who_is_mentioned.append(text[word_pos + 1])
				word_pos += 1
		if text[word_pos] == 'us': # Since names must be Capital, I dont need to check if us is a Sir_Name
			for sir in list_of_sirs:
				who_is_mentioned.append(sir)

		# Finding type of status claim
		if text[word_pos] == 'Knight' or text[word_pos] == 'Knights':
			if text[word_pos - 1] != 'Sir': # Just making sure its not a name like 'Sir Knight'
				status_claim = 1
		if text[word_pos] == 'Knave' or text[word_pos] == 'Knaves':
			if text[word_pos - 1] != 'Sir':
				status_claim = 0

		# Finding type of statement
		if text[word_pos] == 'one':
			if text[word_pos - 1] == 'least':
				type_of_statement = 1
			if text[word_pos - 1] == 'most':
				type_of_statement = 2
			if text[word_pos - 1] == 'exactly' or text[word_pos - 1] == 'Exactly':
				type_of_statement = 3
		if text[word_pos] == 'I' and text[word_pos + 1] == 'am':
			type_of_statement = 5
		if text[word_pos] == 'is' and text[word_pos + 1] == 'a':
			if len(who_is_mentioned) == 1:
				type_of_statement = 6
			else:
				type_of_statement = 7
		if text[word_pos] == 'are':
			if text[word_pos + 1] in ['Knight', 'Knights', 'Knave', 'Knave']:
				if len(who_is_mentioned) == len(list_of_sirs):
					type_of_statement = 4
				else:
					type_of_statement = 8
		word += 1
	return sorted(who_is_mentioned), type_of_statement, type_of_claim

# -------------------------------------------------------------- process_claim fn ------------------------------------------------------------
# Within this statement, also pass through find_sirs to find sirs mentioned
# DOUBLE CHECK ASSUMPTION THAT ONLY 1 statement type can be in a statement
# Also, that only 1 can be in statement (i.e. cant say 'Sir Jack is a Knight and Sir Jill is a Knave')
# This function would then append a list of tuples to dictionary of statements

def process_claim (list_of_sirs, dictionary_of_claims, who_spoke, who_is_mentioned, type_of_statement):
	knight_or_knave = []
	for sir in range(len(list_of_sirs)):
		knight_or_knave.append([0, 1])
	# Then, given who is speaking, set their element to just 1 or 0 rather than [0, 1] # To account for fact their speaking status cant be different than tuple status
	# THen process based on speech type


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
# Find all solutions by processing dictionary_of_claims 
	# We need to test if each solution for one person matches a solution from other sirs
	# If not, then we have conflicting statements, something one person said cant be a truth; they are speaking gibberish
	# If only one person spoke, in which case their statements is the solutions

def find_solutions (list_of_sirs, dictionary_of_claims, solutions_list):
	if not dictionary_of_claims: # Nobody spoke, so return none, ending function
		return

	sirs_who_spoke = list(dictionary_of_claims.keys())
	first_sir, rest_of_sirs = sirs_who_spoke[0], sirs_who_spoke[1:] # Only need to check statements from first sir vs the rest

	# This code is for if someone spoke
	for truth in range(0,2): # Checking Knave Tuples then Knight Tuples
		for solution in dictionary_of_claims[first_sir][truth]:
			if rest_of_sirs == []: # Nobody else spoke
				solutions_list.append(solution) # If nobody else spoke, all solutions are valid
			for other_sirs in rest_of_sirs: # So I skip the first person since that is themself
				if solution in dictionary_of_claims[other_sirs][0]:
					continue # to the next sir
				elif solution in dictionary_of_claims[other_sirs][1]:
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

# If my hunch is correct, then I can use if tuple in next, for just one person, since if the statements by another person arent in the first person,
	# --> they are automatically false

# AND OTHER TESTING I CAN THINK OF...

# ------------------------------------------------------------------- CODE BODY -----------------------------------------------------------------

text = ['.'] # dont have to adjust parsing or sentence checking. Can also remove later
list_of_sirs = [] # Since lists are ordered, I prefer to use lists. Just check for duplication before adding an element
dictionary_of_claims = {} # Need to store names # Actually dont need to store true or false assumptions. That will match pos of name in tuple
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
	list_of_sirs = find_sirs(text, list_of_sirs)

	# Fill dictionary_of_claims
#	process_speech(text, list_of_sirs, dictionary_of_claims)

	# Find solutions given someone spoke
#	find_solutions(list_of_sirs, dictionary_of_claims, solutions_list)

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
			if solutions_list[0][sir] == 0:
				print('Sir', list_of_sirs[sir], 'is a Knave.')
			else:
				print('Sir', list_of_sirs[sir], 'is a Knight.')
# ----------------------------------------------------------------------------------------------------------------------------------------------







