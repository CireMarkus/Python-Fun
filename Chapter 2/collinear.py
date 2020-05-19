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

if (slopeA == slopeB) and (slopeB == slopeC):
	print('Your points are collinear.')
else:
	print('These points are not collinear.')