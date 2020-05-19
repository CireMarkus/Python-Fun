def prime(terms):
	i = 1
	while i <= terms:
		prime = True
		for y in range(2,10):
			if i != y:
				if i%y != 0:
					prime = True	
				else:
					prime = False
					break
		if prime == True:
			yield i
		i+=1

terms = int(input('Please enter the number of terms\t:'))

for i in prime(terms):
	print(i)
