import sys
def sort(L):
	i=0
	while(i<len(L)-1):
		print('\nIteration:\t',i,'\n')
		j=0
		flag = 0
		while(j<(len(L)-i-1)):
			if(L[j]>L[j+1]):
				flag = 1
				temp=L[j]
				L[j] = L[j+1]
				L[j+1] = temp
			j=j+1
		print(L)
		if(flag==0):
			break
		i=i+1
	return(L)
L=[]
#This edit keeps the program from taking the script name as an argument
for x in range (1, len(sys.argv)):
	L.append(int(sys.argv[x]))
print('Before sorting:\t',L)
print(sort(L))