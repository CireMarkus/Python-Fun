n = input('Enter the number of rows: ')
m = int(n)
for i in range(m):
	for j in range(i+1):
		print(i+1, end=" ")
	print()