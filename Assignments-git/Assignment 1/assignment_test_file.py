# Assignment_test_file.py
# Just testing how different functions work here

def testing_continue():
	for num in range(10):
		if num % 2 == 0:
			continue
		elif num == 5:
			break
		print (num)

testing_continue()

def testing_and_or_combination ():
	def if_or_test (a,b,c,d):
		print (a,b,c,d, '--> ', end = '')
		if (a == 1 and b == 2) or (c == 3 and d == 4):
			print ('success')
		else:
			print ('failure')

	if_or_test(1,1,1,1) #F
	if_or_test(1,2,1,1) #S
	if_or_test(1,1,3,1) #F
	if_or_test(1,1,1,4) #F
	if_or_test(1,1,3,4) #S
	if_or_test(0,2,3,1) #F
	if_or_test(0,2,1,4) #F

# testing_and_or_combination()

def list_splicing ():
	# Just checking list splicing
	test_list = [1]
	first, others = test_list[0], test_list[1:]
	print (first)
	print (others)

# list_splicing()

def accessing_dict_of_dict_of_lists():
	test_dict = {'John':{0:[(1),(0)], 1:[(1),(0)]}, 'Jack':{0:[(1),(0)], 1:[(1),(0)]}}

	# Accessing first key in a dictionary, doesnt matter which i access
	print (list(test_dict)[0])
	

# accessing_dict_of_dict_of_lists()

def list_split ():
	# Testing parsing a split of a list
	test_list = [1,2,3,4,5]
	start = 1
	end = 3
	# Should print [2, 3] <-- yep
	print (test_list[start:end])

	#What about into a function
	def addition (test_list, start, end):
		adding = 0
		for element in range(start, end):
			adding += test_list[element]
		print (adding)

	addition(test_list, start, end)
	# Yep, so we can also pass through a function

#list_split()

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