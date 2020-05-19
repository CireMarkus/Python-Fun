testString = 'the quick brown fox jumps over the lazy dog.'

asciiSum = 0
for i in testString:
	asciiSum+=int(ord(i))

print('the total of the ascii values is:\t',asciiSum)