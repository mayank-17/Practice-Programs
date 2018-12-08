'''test=int(input())
while test>0:
    N,a,b,c=map(int,input().split())
    count=0
    m1.append(a)
    m1.append(b)
    m1.append(c)
    max(m1)
    for x in range (1,a+1):
        for y in range(1,b+1):
            for z in range(1,c+1):
                if x*y*z == N:
                    count+=1 
    print (count)
    test=test-1
''''''
from functools import reduce
def factors(n,a,b,c):
    m1=[]
    m1.append(a)
    m1.append(b)
    m1.append(c)
    return set(reduce(list.__add__,([i, n//i] for i in range(1, int(pow(n, 0.5) + 1)) if n % i == 0)))
print(factors(497296800,1000000,1000000,1000000))'''

def nu_of_factors1(n):
    m1=[]
    m1.append(1000000.0)
    m1.append(1000000.0)
    m1.append(1000000.0)
    result_set = set()
    sqrtn = int(n**0.5)
    for i in range(1,sqrtn+1):
        q, r = n/i, n%i
        if r == 0 and q<=max(m1) and i <= max(m1):
            result_set.add(q)
            result_set.add(i)
    l1=list(result_set)
    l1.sort()
    return l1
print(nu_of_factors1(497296800))
'''def triples(N,a,b,c):
    li=[]
    li=factors(N)
    for i in li:'''
        
