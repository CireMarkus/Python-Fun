f1 = open('Textfile.txt','r')
f2 = open('Textfile2.txt','w')
L = []
for x in f1.read():
	L.append(x)

f1.close()

for x in L:
	f2.write(x)
	print(x,end=' ')

f2.close()