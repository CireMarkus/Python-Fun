#This program finds out if the number entered is a perfect square.



def square (num):
	#print('here')
	for i in range (num,0,-1):
		#print('here 1')
		if (i * i) == num:
			#print('here 2')
			return True
	return False
#had some issues with the function, seemed that the language wouldn't enter the loop 
#unless specified it should count down.

user = int(input('Please enter an integer: '))

if square(user) == True:
	print('The number you entered is a perfect square.')
else:
	print('The number youy entered is not a perfect square.')