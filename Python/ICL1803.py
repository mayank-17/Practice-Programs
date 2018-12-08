def sub(b,z):
    cnt=0
    for i in range(len(b)+1):
        for j in range(len(b)-i+1):
            x=list(set(list(b[j:j+i])))
            x.sort()
            #print(b,x,z)
            if(x==z):
                cnt+=1
    return cnt            
	
test=int(input())
while test>0:
	strA=list(input())
	strB=list(input())
	Q=int(input())
	while Q>0:
		op=[]
		qr=list(input().split(" "))
		if qr[0] == '1':
			strA[int(qr[1])-1]=qr[2]
		elif qr[0] == '2':
			strB[int(qr[1])-1]=qr[2]
		elif qr[0] == '3':
			l=int(qr[1])
			r=int(qr[2])
			z=list(set(strA[l-1:r]))
			z.sort()
			strB="".join(strB)
			print(sub(strB,z))
		Q-=1
	test-=1		