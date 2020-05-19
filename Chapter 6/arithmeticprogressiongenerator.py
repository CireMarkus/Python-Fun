def progression(numA, dif, terms):
	for i in range (terms):
		yield (numA+i*d)

a = int(input('Enter the first term of the sequence\t:'))
d = int(input('Enter the common difference of the sequence\t:'))
n = int(input('Enter the number of terms for the sequence\t:'))

ap = progression(a,d,n)

print(list(ap))
