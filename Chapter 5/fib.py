def fib(n):
	if n == 1:
		return 1
	elif n == 2:
		return 1
	else:
		return (fib(n-1) + fib(n-2))

n = int(input('Enter the number of the sequence: '))

for i in range(n):
		print(fib(i))