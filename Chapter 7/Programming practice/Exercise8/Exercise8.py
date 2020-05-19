f1 = open('Exercise8_text.txt','r+')

text = str(f1.read().lower())

text=text.split()

user = str(input('What word would you like to check the frequency of?:\t'))

count = 0

for i in text:
	if i == user:
		count+= 1


print('The word "',user,'" occured ',count,' times')

