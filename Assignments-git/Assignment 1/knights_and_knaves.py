# COMP9021 Assignment 1
# Christopher Lam
	# Not the prettiest...
	# Try to implement truth table next time, as well as replace with regex (not sure how else to be more concise)
	# Also, problem in code in which if list is no longer insertion ordered in python, this will case bugs

import os
import re
from itertools import product

# Save as proper ass1 name
# Submit to website
# Test with tutor and other tests
# Any other changes and resubmit
# One quick check again just before due date/time

#import time
#start = time.time()
#end = time.time()
#print (end - start)

# -------------------------------------------------------------- text_split fn ------------------------------------------------------------
# Splits text into a list of words and punctuation

def text_split (file, text):
	for line in file: # Each line in in iterator is just a str
		line = line.replace('?', '.')
		line = line.replace('!', '.')
		line = line.replace('\n', ' ')
		line = line.replace('\t', ' ')
		line = line.replace(',', ' ') # <----------------- NOTE this is only ok if ',' has no special difference in speech comprehension and if 2 forms cant exist
		line_list = line.split(' ')
		for word in line_list:
			split = re.search('([\".?!,:]*)([a-zA-Z]*)([\".?!,:]*)', word)
			text += list(split.groups())
	text.extend(['.', '.']) # Just to control for potential overflow if text doesnt end with punctuation # Realistically, move this into potential overflow fn
	while True: # Removing extra '' in list created by * in regex
		try:
			text.remove('')
		except:
			break
# -------------------------------------------------------------- find_sirs fn ------------------------------------------------------------
# Used to find all sirs in text

def find_sirs (text, list_of_sirs):
	word_pos = 0
	while word_pos < len(text): # Allows situational double jumps
		if text[word_pos] == 'Sir':
			if text[word_pos + 1] not in list_of_sirs:
				list_of_sirs.append(text[word_pos + 1])
			word_pos += 1
		elif text[word_pos] == 'Sirs':
			while text[word_pos + 1] != 'and':
				if text[word_pos + 1] not in list_of_sirs:
					list_of_sirs.append(text[word_pos + 1])
				word_pos += 1
			word_pos += 1
			if text[word_pos + 1] not in list_of_sirs:
				list_of_sirs.append(text[word_pos + 1])
			word_pos += 1
		word_pos += 1
	return sorted(list_of_sirs)

# -------------------------------------------------------------- sub fns for process_speech fn ------------------------------------------------------------
def find_who_spoke (text, start_of_sentence, end_of_sentence, start_of_speech, end_of_speech):
	who_spoke = None
	for word_pos in range(start_of_sentence, end_of_sentence):
		if word_pos < start_of_speech or word_pos > end_of_speech:
			if 'Sir' in text[word_pos]:
				who_spoke = text[word_pos + 1]
				break
	return who_spoke

def find_what_is_mentioned (text, list_of_sirs, who_spoke, who_is_mentioned, start_of_speech, end_of_speech):
	# NOTE: Shouldve replaced with regex. It would be neater
	# Finds:
		# Whos is mentioned
		# type_of_claim: Knight(1) or Knave(0)
		# type_of_statement:
			# 1 --> At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
			# 2 --> At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
			# 3 --> Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
			# 4 --> All/all of us are Knights/Knaves
			# 5 --> I am a Knight/Knave
			# 6 --> Sir Sir_Name is a Knight/Knave
			# 7 --> Disjunction_of_Sirs is a Knight/Knave
			# 8 --> Conjunction_of_Sirs are Knights/Knaves

	word_pos = start_of_speech
	type_of_statement = None
	type_of_claim = None
	while word_pos < end_of_speech:
		# Finding who is mentioned
		if text[word_pos] == 'I':
			if text[word_pos - 1] != 'Sir': # Since technically 'I' can be a name --> 'Sir I'
				who_is_mentioned.append(who_spoke)
		if text[word_pos] == 'Sir':
			who_is_mentioned.append(text[word_pos + 1])
		if text[word_pos] == 'us': # Since names must be Capital, I dont need to check if us is a Sir_Name
			for sir in list_of_sirs:
				who_is_mentioned.append(sir)

		# Finding type of status claim
		if text[word_pos] in ['Knight', 'Knights']:
			if text[word_pos - 1] != 'Sir': # Just making sure its not a name like 'Sir Knight'
				type_of_claim = 1
		if text[word_pos] in ['Knave', 'Knaves']:
			if text[word_pos - 1] != 'Sir':
				type_of_claim = 0

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
			if type_of_statement not in [1, 2, 3]:
				if len(who_is_mentioned) == 1: # Only 1 Sir has been mentioned
					type_of_statement = 6
				else: # More than 1 Sir has been mentioned
					type_of_statement = 7
		if text[word_pos] == 'are':
			if text[word_pos + 1] in ['Knight', 'Knights', 'Knave', 'Knaves']:
				if len(who_is_mentioned) == len(list_of_sirs): # Everyone has been mentioned
					type_of_statement = 4
				else:
					type_of_statement = 8
		word_pos += 1
	return sorted(who_is_mentioned), type_of_statement, type_of_claim

# -------------------------------------------------------------- process_claim fn ------------------------------------------------------------
# Given information found in process_speech, add solutions to dictionary_of_claims
			# 1 --> At/at least one of Conjunction_of_Sirs/us is a Knight/Knave
			# 2 --> At/at most one of Conjunction_of_Sirs/us is a Knight/Knave
			# 3 --> Exactly/exactly one of Conjunction_of_Sirs/us is a Knight/Knave
			# 4 --> All/all of us are Knights/Knaves
			# 5 --> I am a Knight/Knave
			# 6 --> Sir Sir_Name is a Knight/Knave
			# 7 --> Disjunction_of_Sirs is a Knight/Knave
			# 8 --> Conjunction_of_Sirs are Knights/Knaves
		# type_of_claim = 1 --> Knight
		# type_of_claim = 0 --> Knave

def process_claim (list_of_sirs, dictionary_of_claims, who_spoke, who_is_mentioned, type_of_statement, type_of_claim, solutions_list):
	# Generating all possible solutions
	knight_or_knave = []
	for sir in range(len(list_of_sirs)):
		knight_or_knave.append([0, 1])
	all_solutions = list(product(*knight_or_knave))
	solutions = []								# solutions   <-- Solutions assuming speaker is truthful
	alternative = []							# alternative <-- Solutions assuming speaker is lying

	# Index of speaker and people mentioned
	sirs_mentioned = []
	speaker_pos = list_of_sirs.index(who_spoke)
	for sir_mentioned in who_is_mentioned:
		sirs_mentioned.append(list_of_sirs.index(sir_mentioned)) # So coverting sirs_mentioned from str to list_of_sirs list index

	# Filling solutions into the solutions or alterantive
	for solution in range(len(all_solutions)):
		num_knights = 0
		for sir in sirs_mentioned: # so num_knights == number of those mentioned who are knights
			num_knights += all_solutions[solution][sir]
		num_knaves = len(sirs_mentioned) - num_knights

		if type_of_statement in [1, 7]: # One or more of mentioned is claim
			if (num_knaves >= 1 and type_of_claim == 0) or (num_knights >= 1 and type_of_claim == 1):
				solutions.append(all_solutions[solution])
			else:
				alternative.append(all_solutions[solution])
		if type_of_statement in [2]: # One or zero of mentioned is claim
			if (num_knaves < 2 and type_of_claim == 0) or (num_knights < 2 and type_of_claim == 1):
				solutions.append(all_solutions[solution])
			else:
				alternative.append(all_solutions[solution])
		if type_of_statement in [3, 5, 6]: # One of mentioned is claim
			if (num_knaves == 1 and type_of_claim == 0) or (num_knights == 1 and type_of_claim == 1):
				solutions.append(all_solutions[solution])
			else:
				alternative.append(all_solutions[solution])
		if type_of_statement in [4, 8]: # All mentioned are claim
			if (num_knaves == len(sirs_mentioned) and type_of_claim == 0) or (num_knights == len(sirs_mentioned) and type_of_claim == 1):
				solutions.append(all_solutions[solution])
			else:
				alternative.append(all_solutions[solution])

	# Delete solutions which dont match assumed status when speaking
	solutions_check = 0
	while solutions_check < len(solutions):
		if solutions[solutions_check][speaker_pos] != 1:
			solutions.remove(solutions[solutions_check])
		else:
			solutions_check += 1
	alternative_check = 0
	while alternative_check < len(alternative):
		if alternative[alternative_check][speaker_pos] != 0:
			alternative.remove(alternative[alternative_check])
		else:
			alternative_check += 1

	# Now, if both are empty, then no solution (nothing they said generates a potentially valid solution)
	if solutions == [] and alternative == []:
		solutions_list.append('No solution')
		return

	# Pass into dictionary_of_claims based on whether they spoke before
	if who_spoke not in dictionary_of_claims: # They have not spoken before
		dictionary_of_claims[who_spoke] = {0:[], 1:[]}
		dictionary_of_claims[who_spoke][0].extend(alternative)
		dictionary_of_claims[who_spoke][1].extend(solutions)
	else: # They have spoken before
		new_solutions = []
		new_alternative = []
		for solution in dictionary_of_claims[who_spoke][0]:
			if solution in alternative:
				new_alternative.append(solution)
		for solution in dictionary_of_claims[who_spoke][1]:
			if solution in solutions:
				new_solutions.append(solution)
		dictionary_of_claims[who_spoke][0] = new_alternative
		dictionary_of_claims[who_spoke][1] = new_solutions

# -------------------------------------------------------------- process_speech fn ------------------------------------------------------------
# Given text, find sentences, process, then pass into process_claims to fill dictionary_of_claims
def process_speech (text, list_of_sirs, dictionary_of_claims, solutions_list):
	start_of_sentence = 0
	end_of_speech = 0
	speech_found = False

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
				who_spoke = None
				who_is_mentioned = []
				who_spoke = find_who_spoke(text, start_of_sentence, end_of_sentence, start_of_speech, end_of_speech)
				who_is_mentioned, type_of_statement, type_of_claim = find_what_is_mentioned(text, list_of_sirs, who_spoke, who_is_mentioned, start_of_speech, end_of_speech)
				process_claim(list_of_sirs, dictionary_of_claims, who_spoke, who_is_mentioned, type_of_statement, type_of_claim, solutions_list)
			start_of_sentence, speech_found = end_of_sentence, False # resetting

# -------------------------------------------------------------- find_solutions fn ------------------------------------------------------------
# Find all solutions by processing dictionary_of_claims 
	# We need to test if each solution for one person matches a solution from other sirs
	# If not, then we have conflicting statements, something one person said cant be a truth; they are speaking gibberish
	# If only one person spoke, in which case their potential solutions is the final solutions

def find_solutions (list_of_sirs, dictionary_of_claims, solutions_list):
	if not dictionary_of_claims: # Nobody spoke, so return none, ending function
		return
	# Else, somebody spoke
	sirs_who_spoke = list(dictionary_of_claims)
	first_sir, rest_of_sirs = sirs_who_spoke[0], sirs_who_spoke[1:]
	for state in [0, 1]: # Checking Knave Tuples then Knight Tuples
		for solution in dictionary_of_claims[first_sir][state]:
			solution_check = True # Becomes False if a solution is found invalid
			for other_sirs in rest_of_sirs: # So I skip the first person since that is themself # If nobody spoke, this wont run
				if (solution in dictionary_of_claims[other_sirs][0]) or (solution in dictionary_of_claims[other_sirs][1]):
					continue # So if a solution (tuple) is found within list of tuples for another person, then it is potentially valid solution and we move to next sir
				else:
					solution_check = False # solution is invalid
			if solution_check == True:
				solutions_list.append(solution) # Solution has been found in all sirs, including if only 1 sir
	if solutions_list == []: # None of the potential solutions matched
		solutions_list.append('No solution')

# ------------------------------------------------------------------- CODE BODY -----------------------------------------------------------------
text = []
list_of_sirs = [] # Since lists are ordered, I prefer to use lists. Just check for duplication before adding an element
dictionary_of_claims = {} # Dictionary with keys [John][KnightOrKnave][list of tuples of potential solutions]
solutions_list = []

file_name = input('Which text file do you want to use for the puzzle? ')
with open(file_name) as file:

	# return a list of words and punctuation in the text
	text_split(file, text)

	# find all sirs in a sorted list
	list_of_sirs = find_sirs(text, list_of_sirs)

	# Fill dictionary_of_claims
	process_speech(text, list_of_sirs, dictionary_of_claims, solutions_list)

	# Find solutions given someone spoke (Dont run fn if something stupid has been stated)
	if 'No solution' not in solutions_list:
		find_solutions(list_of_sirs, dictionary_of_claims, solutions_list)

	# Printing who the sirs are here
	print('The Sirs are: ', end = '')
	for name in list_of_sirs:
		if name != list_of_sirs[-1]:
			print(name, end = ' ')
		else:
			print(name)

	# Printing the solutions here
	if 'No solution' in solutions_list: # Someone spoke gibberish
		print('There is no solution.')
	elif solutions_list == []: # Nobody spoke
		print('There are', 2**(len(list_of_sirs)), 'solutions.')
	elif len(solutions_list) > 1: # More than 1 solution
		print('There are', len(solutions_list), 'solutions.')
	else:
		print('There is a unique solution:') # There is only one solution
		for sir in range(len(solutions_list[0])):
			if solutions_list[0][sir] == 0:
				print('Sir', list_of_sirs[sir], 'is a Knave.')
			else:
				print('Sir', list_of_sirs[sir], 'is a Knight.')
# ----------------------------------------------------------------------------------------------------------------------------------------------