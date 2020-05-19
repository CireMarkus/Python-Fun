import os 

os.mkdir('Created_Directory')
os.chdir('Created_Directory')

f1 = open('This_is_a_testfile.txt','w')
f1.write('Test sentence.')
f1.close()