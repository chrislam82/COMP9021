
import os

text = [''] # dont have to adjust parsing
speaking = False
sentences = []
sirs = []
special_characters = ('\"', '\'', '.', '?', '!', ',', '\n')
with open('test_1.txt') as file: 
	for line in file: # Each line in in iterator is just a str
		print (line)
		line_list = line.split(' ')
		print (line_list)
		for word in line_list:
			current_index = 0
			for char_position in range(len(word)):
				for special_char in special_characters:
					if special_char in word[char_position]: # then special_char is in position--> char_position

						if word[current_index:char_position] not in '':
							text.append(word[current_index:char_position])
						text.append(special_char)
						current_index = char_position + 1
			print (current_index)
			if current_index == 0: # Then we havnt found a special character in word
				text.append(word)
print ()
print (text)
print (' '.join(text))



'''
	print ()
	print ('----- ACTUAL -----')
	special_chars = ' '#('\"', '\'', '.', '?', '!', ',', '\n', ' ')
	for line in file:
		text += [e + special_chars for e in line.split(special_chars) if e in special_chars]
	print (text)
'''





'''
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
'''
