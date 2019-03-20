'''
llist = []

if '' in llist[1:300]:
	print ("fail???")
else:
	print ("success???")
'''

def list_lexicographic_order ():
	countries  = []
	countries.append('Australia')
	countries.append('New Zealand')
	countries.append('America')
	countries.append('France')
	countries.append('Germany')

	print (sorted(countries))

def dictionary_lexicographic_order ():
	countries  = {}
	countries[2012] = ['Australia']
	countries[2012].append('New Zealand')
	countries[2011] = ['America']
	countries[2011].append('Germany')
	countries[2011].append('France')
	countries[2011].append('Bahrain')
	countries[2013] = ['America']
	countries[2013].append('Germany')
	countries[2013].append('France')
	countries[2013].append('Bahrain')
	print('\n'.join(f'    {year}: {sorted(countries[year])}'
						for year in sorted(countries) # already sorted so i dont have to sort countries
				)
		)

def list_access_test ():
	test_list1 = ['Country', 'cID', 'Indicator', 'IID', '2013', '2012', '2017']
	test_list2 = ['Country']

	print('starting test_list1...')
	for data_col in range(4, len(test_list1)):
		print (test_list1[data_col])
		print ("test_list1 done")
	print('starting test_list2...')
	for data_col in range(4, len(test_list2)): # So whats happening here is that if I am out of range or end for range doesnt exist, it simply doesnt execute
		print (test_list2[data_col]) # So even if I get empty line for csv file, I dont get access error
		print ("test_list2 done")

list_access_test()
# dictionary_lexicographic_order()
