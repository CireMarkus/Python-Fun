def product(numA,numB):
	if numB == 1:
		return numA
	else:
		return numA +product(numA,numB-1)

print(product(8,3))