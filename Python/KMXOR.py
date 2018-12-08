
test = int(input())
from itertools import combinations_with_replacement
for i in range(test):
    N, K = map(int, input().split())
    myList = [j for j in range(1,K+1)]
    perList = list(combinations_with_replacement(myList, N))
    maxXOR, XOR, taste = 1, 0, []
    for k in range(len(perList)):
        for l in range(N):
            XOR ^= perList[k][l]
            # print(perList[k][l], sep = ',', end = '')
        # print()
        # print(maxXOR)
        if maxXOR <= XOR:
            # print(perList[k])
            maxXOR = XOR
            # print(maxXOR)
            taste = list(perList[k])        

    [print(taste[k], sep=' ', end=' ') for k in range(len(taste))]
    print()

        
'''


#!/bin/python

import os
import sys

#
# Complete the gradingStudents function below.
#


def solution(m, k):
    if m == 1:
        return k
    if k == 1:
        result = ""
        for i in range(m):
            result += "1 "
        return result[:-1]
    temp = k >> 1
    counter = 1
    while(temp != 0):
        temp = temp >> 1
        counter += 1
    maxvalue = (2**counter)-1
    negation_k = maxvalue ^ k
    result = ""
    if m % 2 == 0:
        if negation_k == 0:
            result = str(k-1)+" "+str(1)
        else:
            result = str(k)+" "+str(negation_k)
        for i in range(m-2):
            result += " 3"
    else:
        if negation_k == 0:
            result = str(k)+" "+str(k)+" "+str(k)
        else:
            if k == 2:
                result = str(2)+" "+str(2)+" "+str(2)
            else:
                temp = 2**(counter-1)
                if temp == k:
                    temp = 2**(counter-2)
                    result = str(k)+" "+str(negation_k-temp)+" "+str(temp)
                else:
                    result = str(k-temp)+" "+str(negation_k)+" "+str(temp)
        for i in range(m-3):
            result += " 3"
    return result


if __name__ == '__main__':

    n = int(input())
    arr = []
    for i in range(n):
        inp = input().split()
        m = int(inp[0])
        k = int(inp[1])
        print(str(solution(m, k)))
'''