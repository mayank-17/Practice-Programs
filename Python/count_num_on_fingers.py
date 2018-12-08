f1,f2,f3,f4,f5=[],[],[],[],[]
num=int(input())
count=1
for i in range(1,num+1):
	if count==1:
		f1.append(i)
		count+=1
		continue
	if count==2:
		f2.append(i)
		count+=1
		continue
	if count==3:
		f3.append(i)
		count+=1
		continue
	if count==4:
		f4.append(i)
		count+=1
		continue
	if count==5:
		f5.append(i)
		count=6
		continue
	if count==6:
		f4.append(i)
		count+=1
		continue
	if count==7:
		f3.append(i)
		count+=1
		continue
	if count==8:
		f2.append(i)
		count+=1
		continue
	if count==9:
		f1.append(i)
		count=2
		continue

if num in f1:
	print(1)
elif num in f2:
	print(2)
elif num in f3:
	print(3)
elif num in f4:
	print(4)
elif num in f5:
	print(5)