from itertools import product
A=map(int,input().split())
B=map(int,input().split())
a=[list(A),list(B)]
a=list(product(*a))
print (a)

