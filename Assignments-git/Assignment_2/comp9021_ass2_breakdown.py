# COMP9021 Ass2
# Due April 28 23:59 (Literally last day of week 10, the Sunday)

# Game of tangram
	# Given pieces, try to match shape i guess...

# So .xml file
	# 2 parts, one for coordinates, other for colour
		# Coordinates non-negative (0,1,2...) # No partial coordinates i guess
	# Same formatting from the looks of it between pieces and shapes
# pieces
	# convex polygons
		# So all corners point outwards
	# n>= 3 sides (So at least a triangle or invalid output(i.e. same 3 coordinates or 3 coordinates with one on line))
	# Basically there technically is no first coordinate, it loops around the coordinates to connect into a polygons
	# Pieces can be joined in two directions
		# So if looping through coordinates, could loop clockwise or anticlockwise
	# Can have different orientations and be flipped over
		# ----------------------------------- CHECK IF DIFFERENT ORIENTATIONS MEANS JUST ROTATE A MULTIPL OF 90 DEGREES!!!! ------------------------------------------
	# Pieces can overlap (meaning one piece on another in .xml with pieces)
		# However, this is irrelevant for assignment2 as we are just looking at pieces individually

# Shapes
	# Does not have to be convex, so corners can point inwards or outwards
	# Assumed to be simple polygons
		# Cannot be for example 2 shapes that just touch edges or corners
			# E.g. think about the number 8 but in square formation, one corner touching the corner of the other (this is not allowed)
		# Cant cross (same as pieces, edges can't cross)

# ------------------------------------------------------------------------------------------------ QUESTION 1 --------------------------------------------------------------
# Question 1
	# Shapes we can just assume satisfy constraints
	# Pieces will need to be checked that they satisfy constraints
		# 1. each piece is convex
		# 2. edges >= 3
		# 3. cant cross
def are_valid(): # <------------- 1st FUNCTION
	pass

>>> from tangram import *

>>> file = open('pieces_A.xml')
>>> coloured_pieces = available_coloured_pieces(file)

>>> are_valid(coloured_pieces)
	# Returns True or False (NOT PRINT!!!)
# ------------------------------------------------------------------------------------------------ QUESTION 2 --------------------------------------------------------------
# Question 2
	# Check if pieces in 2 files are identical
def are_identical_sets_of_coloured_pieces():
	pass

>>> from tangram import *

>>> file = open('pieces_A.xml')
>>> coloured_pieces_1 = available_coloured_pieces(file)

>>> file = open('pieces_AA.xml')
>>> coloured_pieces_2 = available_coloured_pieces(file)

>>> are_identical_sets_of_coloured_pieces(coloured_pieces_1, coloured_pieces_2)
	# Returns True or False (NOT PRINT!!!)
# ------------------------------------------------------------------------------------------------ QUESTION 3 --------------------------------------------------------------
# Question 3

# Check whether pieces in .xml file are a solution to shape in another .xml file

def is_solution ():
	pass

>>> from tangram import *

>>> file = open('shape_A_1.xml')
>>> shape = available_coloured_pieces(file)

>>> file = open('tangram_A_1_a.xml')
>>> tangram = available_coloured_pieces(file)

>>> is_solution(tangram, shape)
	# Returns True or False (NOT PRINT!!!)















