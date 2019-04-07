# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import numpy
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def recursive_grid(triangle_grid, down, down_left, down_right, size = 0):
	triangle_check = numpy.zeros((len(grid[0]) + 4, len(grid[0]) + 4), numpy.int)
	size += 1 # For each check in recursion, we are checking if a triangle of size size + 2 is in grid
	triangle_found = False

	triangle_check[2: -2, 2: -2] =\
	triangle_grid[2: -2, 2: -2] +\
	triangle_grid[(down[0] + 2): (down[0] - 2), (down[1] + 2): (down[1] - 2)] +\
	triangle_grid[(down_left[0] + 2): (down_left[0] - 2), (down_left[1] + 2): (down_left[1] - 2)] +\
	triangle_grid[(down_right[0] + 2): (down_right[0] - 2), (down_right[1] + 2): (down_right[1] - 2)]

	for row in triangle_check:
		if 4 in row:
			triangle_found = True
	if triangle_found == True:
		triangle_grid = numpy.equal(triangle_check, 4).astype(numpy.int)

		return recursive_grid(triangle_grid, down, down_left, down_right, size)	
	return size

def generate_framed_grid (grid):
	framed_numpy_grid = numpy.zeros((len(grid[0]) + 4, len(grid[0]) + 4), numpy.int) # Generate framed grid
	framed_numpy_grid[2: -2, 2: -2] += numpy.not_equal(grid, 0).astype(numpy.int)
	return framed_numpy_grid

def size_of_largest_isosceles_triangle():
	# So input 1 is seed for randint generation
	#  	 input 2 is density, which determines how many 0s and 1s there are

	# grid initially generates a random int between 0 and density of size 10 by 10
	# in display_grid(), passes in grid of ints between 0 and density
				#        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid))))
				# Can replace print in display_grid() to prove that my breakdown is true
		# Int of boolean (is cell != 0?)
			# The more numbers greater than 0 (The higher the density), the more 1s there are in the grid
			# True, since if density = 100, was nearly all 1s, when = 0, all 0s, when = 1, around 50%

	# So this function, given grid, which is generated in main, find the largest isosceles_triangle
		# 1st, transform to 1s and 0s just like in display_grid

	if not grid: # if grid is empty
		return 0
	for row in grid: # If grid is all 0s
		if not any(row):
			return 0

	# Find maximum size for triangle facing each direction
 		# Moving grid in triangle directions (up, down, left, right)
 		# Coordinates are [row][column] so [y][x] --> Reversed direction, also 0,0 in top left corner
	framed_numpy_grid = generate_framed_grid(grid)
	up_size = recursive_grid(framed_numpy_grid, [-1, 0], [-1, -1], [-1, 1])

	framed_numpy_grid = generate_framed_grid(grid)
	down_size = recursive_grid(framed_numpy_grid, [1, 0], [1, -1], [1, 1])

	framed_numpy_grid = generate_framed_grid(grid)
	left_size = recursive_grid(framed_numpy_grid, [0, -1], [-1, -1], [1, -1])

	framed_numpy_grid = generate_framed_grid(grid)
	right_size = recursive_grid(framed_numpy_grid, [0, 1], [-1, 1], [1, 1])

	return max(up_size, down_size, left_size, right_size)



try:
    arg_for_seed, density = (abs(int(x)) for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
print('The largest isosceles triangle has a size of',
      size_of_largest_isosceles_triangle()
     )
