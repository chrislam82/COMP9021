# testing how to find angle between 2 lines

import math

# Question 1:
	# How to find the gradient
# Lets say I am given 2 coordinates
coordinate1 = (0,0)
coordinate2 = (1,1)
coordinate3 = (2,2)
coordinate4 = (1,3)

def find_gradient (coordinate1, coordinate2):
	try:
		gradient = (coordinate1[1] - coordinate2[1]) / (coordinate1[0] - coordinate2[0])
	except:
		return 'vertical line'
	return gradient

def find_degrees (coordinate1, coordinate2, coordinate3, coordinate4):
	gradient1 = find_gradient(coordinate1, coordinate2)
	gradient2 = find_gradient(coordinate3, coordinate4)
	if gradient1 == 'vertical line' or gradient2 == 'vertial line':
		# Do an alternate return where we are comparing to a 90 degree line
		pass
	else:
		numerator = gradient1 - gradient2
		denominator = 1 + gradient1*gradient2
	return math.degrees(math.atan2(numerator, denominator))

def returning_all_angles (polygon):
	# So, given a square, can we return the right angles/ what are the returned angles
	doubled_polygon = polygon * 2

	for index in range(len(polygon)):
		print(find_degrees(doubled_polygon[index], doubled_polygon[index + 1], doubled_polygon[index + 1], doubled_polygon[index + 2]))


square = [(0,0), (1,1), (2,1), (1,0)]
	# So we are returning 45, -45, 45, -45. We need to see how tan for line works exactly
returning_all_angles(square)
	# Seems to work, now just need to control for edge case where gradient is straight
	# In this case, we could
