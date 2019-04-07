Quiz 6

import numpy

size = int(input("Enter a size: "))
initial_grid = numpy.zeroes((size + 2, size + 2), np.int)
triangle_max_size = (size  2) + 1
# THink about this max size, what about even?

# Basically, find the element with the greatest size
# Run the same thing 4 times, 1 for each direction

# Method 1:
	# Keep adding in a triangle shape in one direction

# Method 2:
	# Just add 3 triangles, then run a check for each
	# If value in cell = 4xcurrent check, then larger triangle found, and set value in cell to + 1

initial_grid = numpy.zeroes((size + 2, size + 2), np.int)

# So skip the first and the last ones in grid since they are the frame


def superimposing_triangles (direction)
	# Direction that triangle is pointing; arrow from tip to base
	if direction == 'up':
		x_down = 
		x_down_left = 
		x_down_right = 
	elif direction == 'down':
		down = 
		down_left = 
		down_right = 
	elif direction == 'left':
		down = 
		down_left = 
		down_right = 
	else direction == 'right':
		down = 
		down_left = 
		down_right = 

	for length in range(1, triangle_max_size):
		superimposed_grids[1:-1, 1:-1] = initial_grid[x_down, y_down] + initial_grid[x_down_left, y_down_left] + initial_grid[x_down_right, y_down_right]

	# Logical and_or,
	# Then a check, if no more 1s, then largest length = length + 1
	# Run a grid check
	# Then if no more 1s, return the previous or somethings


# FInally, given this function run, return largest value in list of lists






'''
0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 1 1 0
0 1 1 1 0 1 0
0 0 0 0 0 0 0

0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 2 2 2 2 0
0 1 2 2 2 2 0
0 1 2 2 2 1 0
0 1 1 1 0 1 0
0 0 0 0 0 0 0

0 0 0 0 0 0 0
0 1 1 1 1 0 0
0 1 2 2 2 2 0
0 1 2 3 3 3 0
0 1 2 2 2 1 0
0 1 1 1 0 1 0
0 0 0 0 0 0 0
'''