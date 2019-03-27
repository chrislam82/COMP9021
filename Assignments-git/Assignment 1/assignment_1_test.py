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
		print (line)
		line_list = line.split(' ')
		print (line_list)
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
	return text

# -------------------------------------------------------------- find_sirs fn ------------------------------------------------------------
# Used to find all sirs, also useful for finding sirs in speech
	# Not sure if speech sir search is same implementation though

def find_sirs (text, list_of_sirs):
	word_pos = 0
	print (len(text))
	while word_pos != len(text): # Allows situational double jumps
		print (word_pos)
		if text[word_pos] == 'Sir':
			if text[word_pos] not in list_of_sirs:
				list_of_sirs.append(text[word_pos + 1])
				print (list_of_sirs)
		elif text[word_pos] == 'Sirs':
			while text[word_pos + 1] != 'and':
				if text[word_pos + 1] not in list_of_sirs:
					list_of_sirs.append(text[word_pos + 1])
					print (list_of_sirs)
				word_pos += 1
		word_pos += 1
	list_of_sirs = sorted(list_of_sirs)
			

# ------------------------------------------------------------------- CODE BODY -----------------------------------------------------------------

file_name = input('Which text file do you want to use for the puzzle? ')

list_of_sirs = [] # Since lists are ordered, I prefer to use lists. Just check for duplication before adding an element
text = ['.'] # dont have to adjust parsing or sentence checking. Can also remove later
# special_characters = ('\"', '\'', '.', '?', '!', ',', '\n')        < ------------------# Add more if necessary then also add to regex


with open('test_1.txt') as file:
	# split and replace punction for processing purposes
	punctionation_split(file, text)
	# find all sirs
	find_sirs(text, list_of_sirs)
	print ()
	print (list_of_sirs)
	print ()
	print (text)
	print ()
	print (' '.join(text))
# ----------------------------------------------------------------------------------------------------------------------------------------------







