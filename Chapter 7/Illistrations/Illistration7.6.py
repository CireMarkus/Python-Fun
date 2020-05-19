f=open('Ill7.6.txt','w')
f.write('Hi there how are you')
f.close()
k=int(input('Enter a number: '))
f = open('Ill7.6.txt','r')
f1 = open('Ill7.6.1.txt','w')
for s in f.read():
	for c in s:
# 		print('Character ',c,' Ascii value\t:',ord(c))
 		f1.write(str(chr(ord(c)+k)))
f.close()
f1.close()

f1 = open('Ill7.6.1.txt','r')
f2 = open('Ill7.6.2.txt', 'w')
for s in f1.read():
	for c in s:
# 		print('Character ',c,' Ascii value\t:',ord(c))
		f2.write(str(chr(ord(c)-k)))
f1.close()
f2.close()
print('\nThis is your message encrypted with the key: ', (open('Ill7.6.1.txt').read()))
print('This is your message decrypted with the key: ',(open('Ill7.6.2.txt').read()))
