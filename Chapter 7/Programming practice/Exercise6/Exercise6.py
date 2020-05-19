#opens the exercise file for reading and writing.
f1 = open('Exerise6.txt','w+')
f1.write('the quick brown fox jumps over the lazy dog')
f1.close()

f1=open('Exerise6.txt','r+')

#parses through the file and shows the user what is written.
text = f1.readline()
print(text,'\n\n')
user = str(input('What character would you like to replace?\t:'))
replacement = str(input("What character would you like to replace it with?\t:"))
alteredText = ''

for i in text:
	if i == user:
		alteredText+=replacement
	else:
		alteredText+=i

print('Here is your altered text:\t',alteredText)
f1.write(alteredText)