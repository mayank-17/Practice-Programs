n,k,s=input().split()
n,k,s=int(n),int(k),int(s)
c,o=0,1
if n%k==0:
    for i in range(int(n/k)):   
        n=n-k
        c=c+1
    if c<s:
        print(int(s-c))
    elif c==s:
        print(o)
    elif c>s:
        print(o)
        
    
