string,num=input().split()
from itertools import permutations
permutations=list(permutations(string, int(num)))
permutations.sort()
permutations=set(permutations)
[print ("".join(i)) for i in permutations]