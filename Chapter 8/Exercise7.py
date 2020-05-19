testString = "The quick brown fox jumps over the lazy dog."

print(testString.split())


count = 0

for i in testString.split():
	if i.isalnum() == True:
		count+= 1

print(count)