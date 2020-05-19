import math

print('This program will determine if 3 points that you enter are collinear.')

print('Please enter your first coordinates')
x_coordinate_A = int(input('Please enter the X of the first coordinate: '))
y_coordinate_A = int(input('Please enter the Y of the first coordinate: '))

print('\n\nPlease enter your second coordinates')
x_coordinate_B = int(input('Please enter the X of the second coordinate: '))
y_coordinate_B = int(input('Please enter the Y of the second coordinate: '))

print('\n\nPlease enter the third coordinates')
x_coordinate_C = int(input('Please enter the X of the third coordinate: '))
y_coordinate_C = int(input('Please enter the Y of the third coordinate: '))

slopeA = ((y_coordinate_B - y_coordinate_A)/(x_coordinate_B - x_coordinate_A))
slopeB = ((y_coordinate_C - y_coordinate_B)/(x_coordinate_C - x_coordinate_B))
slopeC = ((y_coordinate_C - y_coordinate_A)/(x_coordinate_C - x_coordinate_A))

distanceA = math.sqrt(((x_coordinate_B - x_coordinate_A)**2)+((y_coordinate_B - y_coordinate_A)**2))#distance between point AB
distanceB = math.sqrt(((x_coordinate_C - x_coordinate_B)**2)+((y_coordinate_C - y_coordinate_B)**2))#distance between point BC
distanceC = math.sqrt(((x_coordinate_C - x_coordinate_A)**2)+((y_coordinate_C - y_coordinate_A)**2))#distance between point AC

if (slopeA == slopeB) and (slopeB == slopeC):
	print('Your points are collinear.')
else:
	print('These points are not collinear.')
	if((distanceA and distanceB) == distanceC):
		print('The points make a equilateral triangle.')
	elif((distanceA != distanceB)and(distanceB != distanceC)and(distanceA != distanceC)):
		print('The points make a scalene triangle.')
	else:
		print('The points make a isoscels triangle.')		
