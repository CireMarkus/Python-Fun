#This program reversees the order of a number entered 
num = input('Please enter a number: ')
r_num = str(num)[len(str(num))::-1]
print('The number you entered is ' + num + ' the reverse is ' + r_num)