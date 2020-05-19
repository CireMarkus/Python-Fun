#Creates a file called practiceSentence.txt for read and write access.
f1 = open('practiceSentence.txt','w')
#Writes the sample sentence to the file.
f1.write('the quick brown fox jumps over the lazy dog')
f1.close()

f1 = open('practiceSentence.txt','r')
f2 = open('ascii.txt','w')



#reads the characters from the file to a list
for x in f1.read():
	for c in x:
		print('Chatacter:',c,'(',ord(c),')')
		f2.write('Character:'+str(c)+'('+str(ord(c)) +')'+'\n')

f1.close()
f2.close()

