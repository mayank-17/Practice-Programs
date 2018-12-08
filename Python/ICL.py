def finder(b,z):
    cnt=0
    print("length:",len(b))
    for i in range(len(b)+1):
        for j in range(len(b)-i+1):
            x=list(set(list(b[j:j+i])))
            x.sort()
            #print(b,x,z)
            if(x==z):
                cnt+=1
    return cnt            
            
 
for _ in range(int(input())):
    a=list(input())
    b=list(input())
    q=int(input())
    for i in range(q):
        x=list(input().split())
        if(x[0]=='1'):
            a[int(x[1])-1]=x[2]
            
        if(x[0]=='2'):
            b[int(x[1])-1]=x[2]
            
        if(x[0]=='3'):
            l=int(x[1])
            r=int(x[2])
            z=list(set(a[l-1:r]))
            z.sort()
            print(z)
            y=''.join(b)
            print(y)
            cnt=finder(y,z)
            print(cnt)         
