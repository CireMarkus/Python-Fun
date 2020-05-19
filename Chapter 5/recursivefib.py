def fib(num):
	if num == 1:
		return 1
	elif num == 2:
		return 1
	else:
		return fib(num - 1) + fib(num - 2)

num = int(input('How deep do you want the fibonacci sequence to go: '))

for i in range (1,num):
	print(fib(i))