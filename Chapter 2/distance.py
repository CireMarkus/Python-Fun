import math

print('This program finds the distance betwween two coordinate points.')

print('Please enter the first X coordinate')
oneX = int(input())
print ('Please enter the second X coordinate')
twoX = int(input())
print('Please enter the frist Y coordinate')
oneY = int(input())
print('Please enter the second Y coordiante')
twoY = int(input())

distance = math.floor(math.sqrt(((twoX - oneX)**2) + ((twoY - oneY)**2)))

print('The distance between the the two points is '+ str(distance))