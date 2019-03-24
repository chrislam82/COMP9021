# 30sec/test as usual
# So only one person speaking
# If nobody speaking, then purpose is mainly to point out how many people there might be

def string_split_function(string): # Given a string, split if punctuation found
	pass

# ['.', 'I', 'have', 'just', 'seen', 'Sirs', 'Sanjay', 'and', 'Eleonore!\n', '"I', 'am', 'a', 'Knave,"', 'whispered', 'Sir', 'Eleonore.\n', 'Who', 'is', 'a', 'Knight', 'and',
#'who', 'is', 'a', 'Knave?\n']

# Note, check other special case chars too like \t (might evaluate to space and thus eliminated during split)
def parsing_text_file(file, text):
	for line in file: # converting each line to list
		line_list = line.split(' ')
		for word in line_list:
			word_start = 0 # start of string
			for char_position in range(len(word)):
				for special_char in ('\"', '\'', '.', '?', '!', ',', '\n'): # easier this way as we get to store special_char; not using if would still have to loop through tuple
					if special_char in word[char_position]:
						text.append(word[0:char_position])
						text.append(special_char)
						#word = word[0:char_position]
						#char_position = 0
	print (text)


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

def finding_sirs_and_sentences(text):
	for string in text:
		if 'sir' in string:
			print ('found string:', string)
			# some processing based on finding sir, knight and/or knave in sentence
				# Should probably do a prelim table
				# THere is always a chance that a sir is not mentioned in any quotes but mentioned in general text
				# In which case, they could either be a knight or knave
			# Check the rules, but i think store 4 temp values, 2 for start and end of sentence, 2 for start and end of speech
			# Find sir in outside of speech but inside of sentence
			# Create truth statement based on sir outside telling truth or lying
		if string in ('\"', '.', '?', '!', ','):
			#end of sentence
			#Then we can find who is speaking
			pass
			# All names following Sir capitalised. I think
			# If true, then easier to find
			# Names cant start without Sir and only other possible other capital is start of sentence which at most has to be Sir since Sir MUST precede names

def processing_comments(text, sentences):
	for string in text:
		continue
# ------------------------------------- CODE BODY -----------------------------------

import os

text = ['.'] # dont have to adjust parsing
speaking = False
sentences = []
sirs = []
with open('test_1.txt') as file:
	''' opens as a bunch of strings
	for element in file:
		print (element)
	'''
	parsing_text_file(file, text)
#	sirs, sentences = finding_sirs_and_sentences(text)
#	processing_comments(text,)

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
