import math
'''This program will calculate the angels of a triangle'''

'''The use enters their  coordinates here.
	They are assigned to a tuple named for the vertices.'''
print('Please enter your first coordinate')
x_coordinate_A = int(input('Please enter the X of the first coordinate: '))
y_coordinate_A = int(input('Please enter the Y of the first coordinate: '))
vertA = (x_coordinate_A, y_coordinate_A)

print('\n\nPlease enter your second coordinate')
x_coordinate_B = int(input('Please enter the X of the second coordinate: '))
y_coordinate_B = int(input('Please enter the Y of the second coordinate: '))
vertB = (x_coordinate_B, y_coordinate_B)

print('\n\nPlease enter the third coordinate')
x_coordinate_C = int(input('Please enter the X of the third coordinate: '))
y_coordinate_C = int(input('Please enter the Y of the third coordinate: '))
vertC = (x_coordinate_C, y_coordinate_C)

'''These are the distancees of the lines squared'''
lineABsq = (((vertB[0] - vertA[0])**2) + ((vertB[1] - vertA[1])**2)) #vertices A & B distance squared
lineBCsq = (((vertC[0] - vertB[0])**2) + ((vertC[1] - vertB[1])**2)) #vertices B & C distance squared
lineACsq = (((vertC[0] - vertA[0])**2) + ((vertC[1] - vertC[1])**2)) #vertices A & C distance squared

angle_a = math.degrees(math.acos((lineBCsq-lineACsq-lineABsq)/(-2 * (math.sqrt(lineACsq))*(math.sqrt(lineABsq)))))
angle_b = math.degrees(math.acos((lineACsq-lineABsq-lineBCsq)/(-2 * (math.sqrt(lineABsq))*(math.sqrt(lineBCsq)))))
angle_c = math.degrees(math.acos((lineABsq-lineACsq-lineBCsq)/(-2 * (math.sqrt(lineACsq))*(math.sqrt(lineBCsq)))))

print('The degree of the angel A with coordinates: ' + str(vertA) + ' is ' + str(angle_a) +'°\n')
print('The degree of the angel B with coordinates: ' + str(vertB) + ' is ' + str(angle_b) +'°\n')
print('The degree of the angel C with coordinates: ' + str(vertC) + ' is ' + str(angle_c) +'°\n')