# Assignment_test_file.py

def string_split ():
	string = '.'
	temp = string.split('.')
	print (temp)

string_split()

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