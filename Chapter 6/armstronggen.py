def armstrong(terms):
	i = 0 
	while i <= terms:
		total = 0
		num = [int(x) for x in str(i)]
		for b in num:
			total += b ** len(num)
		if i == total:
			yield i
		i+=1

for i in armstrong(9):
	print(i)