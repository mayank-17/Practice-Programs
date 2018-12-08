from itertools import combinations
a='hack'
a=sorted(a)
c=list(combinations(a,1))
b=list(combinations(a,2))
[print ("".join(i)) for i in c]
[print ("".join(i)) for i in b]