def sum (numA,numB):
	if(numB == 0):
		return numA
	return sum(numA,numB-1)+1

print(sum(5,10))