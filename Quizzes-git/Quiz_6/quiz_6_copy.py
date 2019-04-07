# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and determines the size of the largest
# isosceles triangle, consisting of nothing but 1s and whose base can be either
# vertical or horizontal, pointing either left or right or up or down.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))

def recursive_grid(size = 0): # default ofsize = 0
	size += 1 # For each check in recursion, size of grid += 1






	
# Checking if a full triangle was found
	# For __ For __:
		# If cell = size * 4:
			# return recursive_grid(size)
	# return (size - 1) # Basically, a triangle of length size was not found, hence the largest was size - 1

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
	for row in range(len(grid)):
		for column in range(len(grid[row])):
			grid[row][column] = int(grid[row][column] != 0)

		# 2nd function to layer grids on top of each other
		# 3rd, evaluate the resulting grid
	pass
    # REPLACE pass WITH YOUR CODE


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
