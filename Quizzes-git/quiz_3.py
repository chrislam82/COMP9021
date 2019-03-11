# Written by Eric Martin for COMP9021



import sys
from random import seed, randint, randrange


try:
    arg_for_seed, upper_bound, length =\
            (int(x) for x in input('Enter three integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
# tests will only use + inputs including 0, so no need to worry about negative

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
# Generates 2 lists of a given length
# given a seed (the 3 integers)
# seed, upper_bound, length
# generating a list of that length using that seed to generate random numbers between 0 and the bound
# 
# Find the longest increasing sequence in the list including wrapping around list when needed (like a circle or ring)
# As we can see in expected output, the same number is considered part of the increasing sequence so 3 3 6 is 3 integers
# What about a list of 0s? 0,0,0,0,0 --> 5
  # Use each element only once
#


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

seed(arg_for_seed)
L_1 = [randint(0, upper_bound) for _ in range(length)]
print('L_1 is:', L_1)
print('The length of the longest increasing sequence\n'
      '  of members of L_1, possibly wrapping around, is:',
      length_of_longest_increasing_sequence(L_1), end = '.\n\n'
     )
L_2 = [randrange(length) for _ in range(length)]
print('L_2 is:', L_2)
print('The maximum integer built from L_2 by jumping\n'
      '  as directed by its members, from some starting member\n'
      '  and not using any member more than once, is:',
      max_int_jumping_in(L_2)
     )


