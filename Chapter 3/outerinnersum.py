'''This program adds and compares the sums of the 1st and 4th digits
with the second and third digits.'''

num = input('Please enter a 4 digit number: ')

num = str(num)

a = num[0]
b = num[1]
c = num[2]
d = num[3]

first = int(a) + int(d)
second = int(b) + int(c)

equal = ' '

if(first == second):
	equal = ' and they are equal.'
else:
	equal = ' and they are not equal'

print('The number you enter is ' + num + 
	' \nthe sum of the first and last digits is ' + str(first) +
	' \nand the sum of the inner two digits is ' + str(second) + equal)