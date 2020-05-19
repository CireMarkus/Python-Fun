text = open('saintPablo.txt','r')

freq = { }

for l in text.read():
	for c in l:
		if c not in freq:
			freq[c] = 1
		else:
			freq[c] += 1


for x, y in sorted(freq.items()):
	print ('The character ',x, ' is used ',y,' times.')


