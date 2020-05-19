print('Enter text, press \'\\e\' to exit')
L = []
i = 1
in1 = input('Line number'+str(1)+'\t:')
while(in1 != '\\e'):
	L.append(in1)
	i=i+1
	in1 = input('Line number'+str(i)+'\t:')
print(L)
f=open('Lines.txt','w')
f.writelines(L)
f.close()
f=open('lines.txt','r')
for x in f.readline():
	print(x, end=' ')
f.close()