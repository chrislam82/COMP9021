# test.py

def length_of_longest_increasing_sequence(L): 
    # Given an list of Length L, find the longest sequence
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
# if length of L2 is 0, output is 0 # eric said either is fine technically, but i prefer to stick to 0

	max_int = 0 # replace with values if greater, else return 0

# So we need to jump elements

	for index in len(range(L)):
		access_check = [False] * len(range(L)) # List of length L to check if accessed element yet
		current_index = index
		current_int = []

		while not access_check[current_index]: # While not True # Not accessed
			current_int.add(str(L[current_index])) # add
			access_check[current_index] = True # So record that element of pos current_index has been accessed
			current_index = L[current_index] # so current_index updates to value in element

		if ''.join(current_int) > max_int: # so turn into a string
			max_int = ''.join(current_int)
	return max_int
# for elements in list
# access, then jump

# append to list
# ''.join(list()), might need to convert to str first before appending to list, not sure if i can do it at join
# then compare with storage






# 2nd Q
# lets say we have a list 3,3,5,3,1,0 <-- values
#                         0,1,2,3,4,5 <-- indexes
# Index 0 == 3-->index 3 == 3 (been here already, so stop) 33
# Index 1 == 3      ''   same  33
# Index 2 == 5--> index 5 == 0-->Index 0 == 3--> index 3==3 (so stop) 5033
# We want the largest number (which is 5033)
# So loop all positions: 0,1,2,3,...
# A quadratic solution is fine, it doesnt have to be smart
# When you start, you have a list. store this
# You just need to check that you havnt been somewhere before
    # Could basically do like sieve, change to T when weve been there before
    # Advised to build a list of numbers
    # ''.join(list) <-- string
# indices are always valid
# doesnt matter if numbers are single digit or not
# check but pretty sure its not twice in a row, its just if we've every visited that element before

# Returning a list of elements
# for i in len(list)
# start at each element
# ''.join(str(list[element]
# store pos counters
# if longest_sequence = temp_sequence
# return longest_sequence
# sieve to [False] * len(list) # TF accessed yet or not
# if element accessed is True on sieve, append to temp
# run comparison

