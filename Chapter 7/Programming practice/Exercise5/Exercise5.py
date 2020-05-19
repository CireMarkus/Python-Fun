import operator

f1 = open('Wolves.txt','r')

freq = {}
word = ''
text = []

for l in f1.read():
	for c in l:
		text.append(c)
for c in range (0,len(text)):
	#print(c, end='')
	if text[c] != ' ' and text[c] != ',' and text[c] != '\n'and text[c] != '?' and text[c]!='.':
		word+=str(text[c])
	else:
		if word not in freq:
			freq[word] = 1
			word = ''
		else:
			freq[word] += 1
		word = ''
		



# for x,y in sorted(freq.items(),key=operator.itemgetter(1)):
# 	print(x,':',y)

user = str(input('enter the word you want to know: '))

if user in freq == True:
	print('the word ',user,' occured ',freq[user],' times.')
else:
	print('Your word didn\'t occur in the text.')