test=int(input())
l=[]
s=''
for i in range(1,test+1):
    s=input()
    l.append(s)
len1=len(l)
sum=0
c1=test-1
check=list(set(l[0]))
for i in check:
    count=0
    for j in range(1,test):
        if i in l[j]:
            count+=1  
    if count == c1:
        sum+=1
print(sum)        