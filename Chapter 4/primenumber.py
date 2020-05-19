#This program will see if the number you enter is a prime number.

import math

#This asks the user to enter a number.
num = int(input("PLease enter a numer: "))

# function to check if the number is prime.
def is_prime(num):
	if num <= 3:
		return num > 1
	elif num % 2 == 0 or num % 3 == 0:
		return False

	i = 5

	while i * i <= num:
		if num % i == 0 or num % (i +2) ==0:
			return False
		i = i + 6
	return True


if is_prime(num) == True:
	print('The number you entered is prime.')
else:
	print('The number is not prime.')