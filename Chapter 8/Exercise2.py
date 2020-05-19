testString = 'The quick brown fox jumps over the lazy dog.'

encodedString = testString.encode('utf-32','strict')

decodedString = encodedString.decode('utf-32')
print(encodedString)
print(decodedString)