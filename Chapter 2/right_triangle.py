import math



print('Please enter your first coordinate')
x_coordinate_A = int(input('Please enter the X of the first coordinate: '))
y_coordinate_A = int(input('Please enter the Y of the first coordinate: '))

print('\n\nPlease enter your second coordinate')
x_coordinate_B = int(input('Please enter the X of the second coordinate: '))
y_coordinate_B = int(input('Please enter the Y of the second coordinate: '))

print('\n\nPlease enter the third coordinate')
x_coordinate_C = int(input('Please enter the X of the third coordinate: '))
y_coordinate_C = int(input('Please enter the Y of the third coordinate: '))

'''slopeA = ((y_coordinate_B - y_coordinate_A)/(x_coordinate_B - x_coordinate_A))
slopeB = ((y_coordinate_C - y_coordinate_B)/(x_coordinate_C - x_coordinate_B))
slopeC = ((y_coordinate_C - y_coordinate_A)/(x_coordinate_C - x_coordinate_A))'''

distanceA = ((x_coordinate_B - x_coordinate_A)**2)+((y_coordinate_B - y_coordinate_A)**2)#distance between point AB
distanceB = ((x_coordinate_C - x_coordinate_B)**2)+((y_coordinate_C - y_coordinate_B)**2)#distance between point BC
distanceC = ((x_coordinate_C - x_coordinate_A)**2)+((y_coordinate_C - y_coordinate_A)**2)#distance between point AC

	

 
if(distanceA > distanceB) and (distanceA > distanceC):
	print('here 1')
	if(distanceB + distanceC) == distanceA:
		print("Your triangle is a right triangle")
		print('here 1.2')
	else:
		print('This triangle is not right angled')
		print('here 1.3')

elif (distanceB > distanceA) and (distanceB > distanceC):
	print('here 2')
	if(distanceC + distanceA) == distanceB:
		print("Your trinangle is a right triangle")
		print('here 2.2')
	else:
		print('This triangle is not right angled')
		print('here 2.3')

elif (distanceC > distanceA) and (distanceC > distanceB):
	print('here 3')
	if(distanceA + distanceB) == distanceC:
		print("Your trinangle is a right triangle")
		print('here 3.2')
	else:
		print('This triangle is not right angled')
		print('here 3.3')

else:
	print('This triangle is not right angled')
	print('here 4')


