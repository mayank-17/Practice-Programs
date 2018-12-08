test=int(input())
for i in range(test):
	n,m=map(int,input().split())
	arr=[]
	sum1=0
	if n==1 and m==1:
		print("Cyborg")
	else:
		l=[]
		for i in range(n):
			row_list=[]
			for j in range(m):
				row_list.append(input().split(" "))
				print(row_list)
				l.append(row_list)
	print(l)
	