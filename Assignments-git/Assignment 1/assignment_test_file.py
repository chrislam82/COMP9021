# Assignment_test_file.py

def string_split ():
	test_list = ['I', 'am', 'here\"', 'now']
	print (test_list)
	for element in test_list:
		if '\"' in element:
			temp = '\"'.split('\"')
			print (temp)
	print (test_list)

string_split()

def list_initial ():
	test_list = ['.']
	print (test_list)
	print (type(test_list))
	test_list += "hello"
	print (test_list)
	print (type(test_list))

#list_initial()