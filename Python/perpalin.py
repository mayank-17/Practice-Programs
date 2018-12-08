for test in range(int(input())):
    string=input()
    alpha=[ [] for i in range(26)]
    for  j in range(len(string)):
        a=ord(string[j])-97
        alpha[a].append(j+1)
    print (alpha)
    s1,s2,s3=[],[],[]
    signal,sig=2,-1
    for i in range(26):
        if len(alpha[i])%2!=0:
            signal-=1
            sig=i
        if signal==0:
            break
    if signal==0:
        print('-1')
        continue
    for i in range(26):
        if i!=sig:
            s1+=alpha[i][:len(alpha[i])//2]
            s2+=alpha[i][len(alpha[i])//2:]
    print (s1,s2)        
    if sig!=-1:
        s3=alpha[sig]
    s1=s1+s3+s2[::-1]
    for k in s1:
        print(k,end=' ')
    print('') 
