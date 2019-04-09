# COMP9021 Asssignment 2

import re

# Steps
	# 1. Determine how to read in .xml files and store
	# 2. Test if inputs are valid
	# 3. Test if


def are_valid(shapes):
	# Check if pieces passed into file are valid

	# Now the question is how to test whether or not the input is valid?
	# What are the rules?
		# 1. edges >= 3
	MINIMUM_EDGES = 3

	for shape in shapes:
		if len(shape[0]) < MINIMUM_EDGES: 
			return False
		# 2. each piece is convex
		# 3. cant cross	
	pass


def are_identical_sets_of_coloured_pieces():
	# Check if pieces in 2 .xml files are identical

	# Questions
	# does colour matter, are we just matching the coordinates or are we also matching colour (doesnt really matter, more for clarity in answer)
	# Can there be more than 1 matching shape?
	# Is rotation only 90 degrees?
		# Is it possible to rotate a shape less than 90 degrees?

	# Compare pieces in the 2 .xml files and compare pairs that are the same colour


	pass

def is_solution ():
	# Check if pieces in 1 .xml file are a solution to shape in another .xml file

	# Question:
		# Do we have to use all the pieces to form shapes
			# E.g. If we only need 2/4 pieces to form shapes, is that still ok?
			# Look at tangram game
	pass

def test_open_file (file_name):
	with open(file_name) as file:
		next(file) # Skip header
#		print ('----- START READING -----')
		# The question here is how to store shapes in .xml file?
		# We want to allow duplication in case 2 shapes with exactly the same coordinates exist (since pieces can overlap)
			# So id say probably store .xml seperately, no need to store in one data structure since that is fixed for each function
			# We also might want to store some extra information about each piece (such as area or other information that determines the angle)
				# So we want a mutable data structure that isnt necessarily ordered (could be though)
				# Doesnt remove duplication so dictionaries and sets are out
			# Therefore for now, I'd go with classes or a list of lists
				# Since we havnt done classes for now, Id just go with list of lists
			# list of lists:
				# 1 we store coordinates, 2 we store colour
				# Question is whether or not colour is important for shape matching?
		shapes = []
		for text in file:
			line = text.split('\"')
			if len(line) == 5: # Then it is not a line with pieces
					# Alternatively, how could i skip the last iteration in an iterator object?
				coordinate_split = line[1].split(' ')
				coordinates = []
				for element in range(len(coordinate_split)):
					try:
						x = int(coordinate_split[element])
						y = int(coordinate_split[element + 1])
						coordinates.append((x,y)) # Trying to get a list of tuples
						continue
					except:
						continue
#				coordinates = [() for element in coordinates]
				shapes.append([coordinates, line[3]]) # Append coordinates and colour to shapes storage
#		print ('----- FINISH READING -----')

		return shapes

def test_assignment ():
	# Function called to test that assignment is working in steps of Task 1,2,3
	pass

def run_assignment ():
	# Function called to test that assignment is working in steps of Task 1,2,3
	pieces_a = test_open_file('pieces_A.xml')
	for element in pieces_a:
		print (element)

test_assignment()
run_assignment()































