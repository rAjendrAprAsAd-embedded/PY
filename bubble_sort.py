import array

'''import array
arr = array.array('i', [10,20,30,40,50])
print(arr)
''' 
ar=array.array('i',[])
x=int(input('enter the value'))
for i in range(0,x):
	num= int(input('Enter value'))
	ar.append(num)
y=x-1
for i in range(0,x):
	k=0
	for j in range(0,y):
		if(ar[j]>ar[j+1]):
			ar[j]=ar[j]+ar[j+1]
			ar[j+1]=ar[j]-ar[j+1]
			ar[j]=ar[j]-ar[j+1]			
			k=k+1
	x=x-1
	if(k==0):
		break
y=y+1
for i in range(0,y):
         print(ar[i])
