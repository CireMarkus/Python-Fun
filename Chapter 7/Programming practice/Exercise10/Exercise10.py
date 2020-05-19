'''This program changes the name of a file to a 
user specified one.'''
import os 

f1 = open('Testfile.txt','w')

f1.write('This is a test file.')

f1.close()

user = str(input('What would you like to rename the text file to?\t:'))

os.rename('Testfile.txt',user+'.txt')