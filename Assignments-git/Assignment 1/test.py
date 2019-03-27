# test.py

from itertools import product

truth_dictionary = {}

# Could instead have elements based on T or F

# So here, we have loop to fill in T or F statements
# Asssuming T, generate truth statement
# Then run a statement comparison, 
# If valid, append to list
# Else, dont append, or maybe just add, then pop at end after a chreck
# Third option is to find andrew fist and check status, if false, continue

# One edge case
# What is andrew says "..." so clearly knave
# Then someone says, andrew is knight, or andrew is knave? would that conflict if i didnt store the alternative (could always store as 3) (if 3, then always ignore)
# This means andrew will generate 1 ignore statement, 1 truth statement

Andrew = [0,0]
Nancy = [1,1]
Bill = [2,1]
Hilary = [2,2]


Z = product(Andrew, Nancy, Bill, Hilary)

#truth_dictionary[Andrew] = []
for element in Z:
	print (element)
# How to append lists to a list?
# Or maybe there is another way to store it


# Question is, how can this be used to generate truth storage?
# Here, we can generate truth statements through product of T or F for each person
# So we can use itertools to generate lists for storage
# We can then store and assign these to each speech
