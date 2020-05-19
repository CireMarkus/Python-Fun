f1 = open('Writingprompt.txt','r+')
f2 = open('Writingprompt2.txt','w')

text = []
newText = []
words = ''
alteredText = []
alteredString = ''

for x in f1.read():
	text.append(x)
for x in range(0,len(text)):
	if text[x] != ' ' and text[x] != '\n':
		words+=text[x]
	else:
		newText.append(str(words))
		words = ''

for x in newText:
	alteredText.append(x[0].upper()+x[1:])

for x in alteredText:
	alteredString += x + ' '

print (alteredString)
f2.write(alteredString)

f1.close()
f2.close()
