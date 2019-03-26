# 30sec/test as usual
# So only one person speaking
# If nobody speaking, then purpose is mainly to point out how many people there might be

# NOTES:
# DOUBLE TEST punctuation_split
	# Especially regex part and think about special case displays of mix of letters and punctuation to create words

import os
import re

def punctionation_split (file, text):
	for line in file: # Each line in in iterator is just a str
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
# NOTE!!! WHAT ABOUT EDGE CASE OF WORD ENDING WITH '
# MAKE SURE I ACCOUNT FOR THAT


# ------------------------------------- CODE BODY -----------------------------------


text = ['.'] # dont have to adjust parsing or sentence checking. Can also remove later
# special_characters = ('\"', '\'', '.', '?', '!', ',', '\n')        < ------------------# Add more if necessary then also add to regex

with open('test_1.txt') as file: 
	punctionation_split(file, text)
	print ()
	print (text)
	print (' '.join(text))
# ---------------------------------------------------------------------------------------
















































	'''
						special_char_position = word.find(special_char) # position of special char in word
						# I could either store positions in a dictionary or something or do it without storing first
						# Storing would give me beneift of doing everything at the end through splitting and dont have to think about the recheck problem
							# Recheck problem might be k if we word and char reset works well with for loop
							# In which case, we wouldnt need to have as complex code
						# Doing everything in one go might be faster


						temp_list = word.split(special_char) # problem with using split is that you lose the special char and dont know where it was located
						print (temp_list[0])
						text.append(temp_list[0])
						#text += temp_list
						# The question here is now how to recheck the word for more special char
						# the rest of the string in temp_list[1]
	'''



#			if '.' in word:
#				temp_list = word.split('.')
#				text.append(temp_list[0])
				# So this works, the question is what if there are 2 punctuation within the sentence
				# The last part becomes, what if there is only one, in which case I end up with whitesapce. Then I would need to delete the whitespace



	'''
					print ("found")
					text.append(word[char])

	for word in text:
		if word == '':
			pass
	print (text)
	test_chat = '.'
	if test_chat in ('\"', '\'', '.', '?', '!', ','):
		print ("found")
		text.append(test_chat)
	'''

	# Alternative method, just check for chars when trying to find truth statements and pop or remove or something before processing
'''
			if '\"' in string:

				temp_string_split = string.split('\"')
			if '\'' in string:
				temp_string_split = string.split('\'')
			if '.' in string:
				temp_string_split = string.split('\"')
			if '?' in string:
				temp_string_split = string.split('\"')
			if '!' in string:
				temp_string_split = string.split('\"')
			if ',' in string:
				temp_string_split = string.split('\"')

			# Doing splitting
			if any(('\"', '\'', '.', '?', '!', ',')) in string:
				print ("found")
	text += [string]
	print (text)

	if ' ' in ...:
		temp_string_split.remove(' ')
	text += temp_string_split
'''
'''
			if string.endswith('\"'):
				text += string.split('\"') +['\"']
			elif string.startswith('\"'):
				text += ['\"'] + string.split('\"')
			if '\n' in string:
				temp_string_split = string.split('\n')
				#print (temp_string_split)
				text += [temp_string_split[0]]
			
'''
# NOTE: theres still a lot of problems here, havnt split end of sentences and stored it
# Also, code above doesnt account for \n and " in same string, so lead to error
# Think about how to store and process first on paper before coding
# At least part of the general parsing of text into a data structure is working for now

# ------------------------------------- OTHER JUNK -----------------------------------



'''
			text += line

		print (line_list)
'''

'''
		if string.endswith(('.','!','?',))

if speaking:

if speaking:
'''

# We could try parse everything once
# Or do a double parse
	# 1st time, to note who is sirs (might be beneficial for data storage generation before inserting T/F stuff) and also to separate " from other things in text
	# Second time for actual generation
