'''This program adds and compares the sums of the 1st and 4th digits
with the second and third digits.'''

num = input('Please enter a 4 digit number: ')

#changes number to a string so numbers can be seperated
num = str(num)

a = num[0]
b = num[1]
c = num[2]
d = num[3]

#add the outer and inner numbers repectivly
first = int(a) + int(d)
second = int(b) + int(c)

#equal flag
equal = ' '
#checks to see if the added sums are equal
if(first == second):
	equal = ' and they are equal.'
	#adds plus one to the center numbers if they are equal
	newnum = 'your new number is ' +a+str(int(b)+1)+str(int(c)+1)+d
else:
	equal = ' and they are not equal'
	newnum = 'there is no new number '

#final print out to the user
print('The number you enter is ' + num + 
	' \nthe sum of the first and last digits is ' + str(first) +
	' \nand the sum of the inner two digits is ' + str(second) + equal+ 
	' \nand ' + newnum)