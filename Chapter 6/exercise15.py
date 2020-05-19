def multipules(terms):
	i=0
	while i <= terms:
		if i%6 == 0:
			yield i
		i+=1

for x in multipules(20):
	print(x)

