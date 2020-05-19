terms = int(input('Enter the number of terms:\t'))
L1 = [i for i in range(1,terms+1)]
L2 = [x**4 for x in L1]

print('L1:\t',L1)
print('L2:\t',L2)