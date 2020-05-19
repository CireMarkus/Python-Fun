#Writes lines of texts to the file
f = open('Ill7.5.txt','w')
f.writelines(['Hi there', 'How are you'])
f.close()

#This snippet reads the first 15 bytes of the file and prints them to the screen
#This causes the print funtion to print 'Hi thereHow are'
f=open('Ill7.5.txt','r+')
str0 = f.read(15)
print('String str\t:',str0)
pos = f.tell()
print('Current postion\t:',pos)

#This code snippet reads the last 5 bytes of the code.
#It then prints the ' you' from the file
str1 = f.read(5)
print('Str1\t:',str1)

pos = f.seek(0, 0) #this moves the seeker to the begining of the file
print('Current position\t:',pos)

str0 = f.read(20) #This reads the full 20 bytes of the file to the str0 variable
print('Again read String is: ', str0)
f.close()