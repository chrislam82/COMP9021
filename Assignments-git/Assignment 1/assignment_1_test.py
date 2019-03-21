# 30sec/test as usual
# So only one person speaking
# If nobody speaking, then purpose is mainly to point out how many people there might be

import os

text = ['.'] # dont have to adjust parsing
speaking = False
with open('test_1.txt') as file:
	''' opens as a bunch of strings
	for element in file:
		print (element)
	'''

	for line in file: # converting each line to list
		line_list = line.split(' ')
		for string in line_list:
			if string.endswith('\"'):
				text += string.split('\"') +['\"']
			elif string.startswith('\"'):
				text += ['\"'] + string.split('\"')
			if '\n' in string:
				temp_string_split = string.split('\n')
				print (temp_string_split)
				text += [temp_string_split[0]]
			else:
				text += [string]
	print (text)
# NOTE: theres still a lot of problems here, havnt split end of sentences and stored it
# Also, code above doesnt account for \n and " in same string, so lead to error
# Think about how to store and process first on paper before coding
# At least part of the general parsing of text into a data structure is working for now


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
