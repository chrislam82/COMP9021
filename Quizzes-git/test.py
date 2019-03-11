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


#for i in range (1,3): # so 1,2,3
#	print (i)
	# prints 1, 2
	# 1, len(L) should print from 1 to len(L) -1 then

print (length_of_longest_increasing_sequence([1,2,3,1,2,3,4]))


'''
1,2,3
starting is index = 1
we plus twice

start at 1
2
3
'''