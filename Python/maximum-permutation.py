#!/bin/python3

import os
import sys

from itertools import permutations as pmt
# Complete the function below.

def maximumPermutation(w, s):
    l=[]
    p=list(pmt(w,len(w)))
    p.sort()
    permut=set(p)
    [l.append("".join(i)) for i in permut]
    m=[]
    for i in l:
    	count=0
    	for j in range(len(s)):
    		st=s[j:j+len(i)]
    		if i in st:
    			count+=1
    	m.append(count)

    if m.count(max(m)) > 1:
        l2=[]
        l3=[]
        for i in m:
            if max(m) == i:
                l2.append(m.index(i))      
        for i in l2:
            l3.append(l[i])
        l3.sort()
        return l3[0]    


    if max(m) == 0:
    	return ('-1')

    else:
        return (l[m.index(max(m))])


if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_i in range(t):
        w = input()

        s = input()

        print(maximumPermutation(w, s))

        #f.write(result + "\n")

    #f.close()
