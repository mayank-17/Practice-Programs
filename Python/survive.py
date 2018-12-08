import math
t=int(input())
while t:
    n,k,s=map(int,input().split(" "))
    na=-1
    f=float((s*k)/n)
    r=math.ceil(f)
    if k>n:
        print(na)
    else:
        d=s/7
        r=(s%7)-1
        t=s*k
        if n*(d*6+r)>=(s*k):
            print(int(r))
        else:
            print(na)
    t=t-1



    
