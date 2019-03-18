def none_test ():
	x = None

	print (x)
	# print (int(x)) # cant convert None to int
	#print (x > 10) # Cant have compare between None
	#print (x < 10)
	#print (x > 10.0) # Cant have compare between Float
	#print (x < 10.0)
	print (x == 0) # False

def float_test ():
	integer = '7'
	integer_float = '5.0'
	floating = '2.34'

	print (int(integer))
	#print (int(integer_float)) # Error
	#print (int(floating)) # Error

	print (float(integer))
	print (float(integer_float))
	print (float(floating))

	print (type(float(integer)))
	print (type(float(integer_float)))
	print (type(float(floating)))

def comparison_empty_string():
	empty = ''
	#convert_int = int(empty)
	#convert_float = float(empty)
	if empty is '':
		print (True)
	else:
		print (False)

comparison_empty_string()
# none_test()
#float_test()

