# test.py

def length_of_longest_increasing_sequence(L): 
    # Given an list of Length L, find the longest sequence
    #Can return 0 for list of length 0,null,no elements
    # can return 1 for list of length 1 element

    longest_sequence = 0 # If L is empty, should return 0

    for starting_index in range(len(L)): # Basically iterating through every index one at a time from 0 to n
        length = 1 # counting the sequence length for each sequence
        current_value = L[starting_index] # value of starting pos

        for movement in range(1, len(L)): # Since we don't iterate on first element itself, will add to pos up to len(L) - 1
            position = starting_index + movement
            if position >= len(L):
              position -= len(L)
            if L[position] >= current_value: # Sequence is increasing
                length += 1
                current_value = L[position] # update value storage
            else:
                break # once we have a smaller value, we break the loop

        if length > longest_sequence: # at end of each index check, if we have a longer length, then update length
            longest_sequence = length

    return longest_sequence 

def max_int_jumping_in(L):
# Half of marks for each
# if output is 010, then that is 10
# if length of L2 is 0, output is 0 # eric said either is fine technically (0 or None), but i prefer to stick to 0

  max_int = 0 # replace with values if greater, else return 0

  for index in range(len(L)): # so run loop for each element
      access_check = [False] * len(L) # List of length L to check if accessed element yet
      current_index = index # starting index
      current_list = [] # list to store values

      while not access_check[current_index]: # While not True # Havn't accessed element
          current_list.append(str(L[current_index])) # add value of current index to list
          access_check[current_index] = True # So record that element of pos current_index has been accessed
          current_index = L[current_index] # so current_index updates to value in L
      current_int = int(''.join(current_list)) # Transform into an int

      if current_int > max_int: # checking if value generated is bigger
          max_int = current_int
  return max_int

def long_test (listt, output):
	assert (length_of_longest_increasing_sequence(listt) == output)
	print (listt)

def max_test (listt, output):
	assert (max_int_jumping_in(listt) == output)
	print (listt)

def actual_long_test ():
	print ('-----------------------')
	long_test([], 0)
	long_test([0], 1)
	long_test([999999999999999999], 1)
	long_test([0,1], 2)
	long_test([1,2,3], 3)
	long_test([1,2,1], 3)
	long_test([1,2,1,2], 2)
	long_test([-1], 1)
	long_test([-1, 0, 1], 3)
	long_test([-1, -2, -3], 2)
	long_test([-3, -2, -1], 3)
	long_test([1,2,3,4,5,6,7,8,9,10,11,12,13,4], 13)
	long_test([1,1,1,1,1,1,1,1,1,1,1,1,1], 13)
	long_test([3,1,2], 3)
	long_test([3,2,1], 2)
	print ()
	print ("long test done")
	print ('-----------------------')
	print ('\n')

def actual_max_test ():
	print ('-----------------------')
	max_test([], 0)
	max_test([0], 0)
	max_test([0,0,0,0,0,0,0,0,0,0,0,0,0], 0)
	max_test([0,0,0,0,0,0,0,0,1,0,0,0,0], 100)
	max_test([0,2,0,0,0,0,0,0,1,0,0,0,0], 1200)
	print ()
	print ("max test done")
	print ('-----------------------')
	print ('\n')

actual_long_test()
actual_max_test()




























