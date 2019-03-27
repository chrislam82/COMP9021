# Assignment_test_file.py
# Just testing how different functions work here

def string_replace ():
	test_string = '1_1_1_1_1_1_1_1_1_1'
	print (test_string.replace('1', '2')) # So replaces all occurrences

	test_string = '1_1_1_1_1_1_1_1_1_1'
	print (test_string.replace('0', '2')) # So fine even if none

# string_replace()

def truth_dictionary_access ():
	from itertools import product

	test_dictionary = {'John':(0,1), 'Jack':(0,0), 'James':(2,1)}
	# In python 3.6, dictionaries are insertion ordered
	# https://stackoverflow.com/questions/39980323/are-dictionaries-ordered-in-python-3-6

#	test_dictionary = sorted(test_dictionary)
#	# Just to make sure
#	# sorting returns a list so invalid
#	print (test_dictionary)
#	print (type(test_dictionary))

	truth_tuple = list(product(*test_dictionary.values()))
	print (truth_tuple)

#	truth_dictionary['John']

	# NOTE
	# 1. Need to make sur that insertion order in test_dictionary is true 						<--- see sorting_dictionary() below
	# 2. Need to make sure that product of values will product in order according to key order in dictionary

#truth_dictionary_access()

def sorting_dictionaries ():
	test_dictionary = {'John':(0,1), 'Jack':(0,0), 'James':(2,1)}

	test_dictionary = sorted(test_dictionary.items())
	print (test_dictionary)

	# So here, we can sort dict.items() to ensure lexi... order

#sorting_dictionaries()

def string_split ():
	string = '.'
	temp = string.split('.')
	print (temp)

#string_split()

def list_initial ():
	test_list = ['.']
	print (test_list)
	print (type(test_list))
	test_list += "hello"
	print (test_list)
	print (type(test_list))

#list_initial()

def find_index_test ():
	word = "bcdeabcdeabcde"
	for count in range(50):
		print (word.find('a')) # Using find because find does not return error whereas index does		

#find_index_test()

def list_of_lists (): # testing if i can append lists to lists
	list_of_lists =[]

	list_of_lists.append([])
	list_of_lists.append([])
	list_of_lists.append([])
	list_of_lists.append([])
	list_of_lists.append([])

	print (list_of_lists)

#list_of_lists()