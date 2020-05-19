# this program finds the factors of the number 
# entered by the user

n = int(input('Please enter a number: '))

i = 1
factors = []
while i <= n:
	if n % i == 0:
		factors.append(i)
	i +=1


print('The factors of '+ str(n) +' are ' + str(factors))