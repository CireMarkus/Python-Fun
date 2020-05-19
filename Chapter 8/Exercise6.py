testString = "The quick brown fox jumps over the lazy dog."

print(testString.split())

keywords = ['False','class','finally','is','return','None','continue',
'for','lambda','try','True','def','from','nonlocal','while','and',
'as','elif','if','or','yield','assert','else','import','pass','break',
'except','in','raise']

count = 0

for i in testString.split():
	if i in keywords:
		count+= 1

print(count)