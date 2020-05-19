#reads the test file and loads it into the program
f1=open('Exercise7_text.txt','r+')
text = ''

for l in f1.readlines():
	text+=l

print('This is the text in the file:\t',text)

user = str(input('What word would you like to replace?:\t'))
replacement = str(input('What would you like to replace it with?:\t'))
alteredText = ''

text = text.split()

for i in range(0,len(text)):
	if text[i] == user:
		alteredText+=replacement+' '
	else:
		alteredText += text[i]+' '

print(alteredText)

f1.write(alteredText)
f1.close()