def product(numA,numB):
	if numB == 0:
		return 1

	else:
		return numA *product(numA,numB-1)

print(product(4,3))