def fib(terms):
	i = 1
	a,b = 0, 1
	while i <= terms:
		yield b
		a, b = b, a+b
		i += 1

for i in fib(10):
	print(i)