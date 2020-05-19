def geometric(a,r,n):
	i = 0
	while i < n:
		yield a*r**i
		i+=1

for i in geometric(1,2,100):
	print(i)