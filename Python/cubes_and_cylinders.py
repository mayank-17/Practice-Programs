#!/bin/python3

import os
import sys


# Complete the function below.

def maximumPackages(S, K, R, C):
    count=0
    '''for i in K:
                    if i != 1:
                        for j in range(1,i+1):
                            S.append(j)'''
    for i in range(len(S)):
        if R[i] >= i:
            count+=1
 
    return count



if __name__ == '__main__':
    #f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])
    m = int(nm[1])

    #S_size = int(input())

    S = list(map(int, input().rstrip().split()))

    #K_size = int(input())

    K = list(map(int, input().rstrip().split()))

    #R_size = int(input())

    R = list(map(int, input().rstrip().split()))

    #C_size = int(input())

    C = list(map(int, input().rstrip().split()))

    result = maximumPackages(S, K, R, C)

    print(result)

    #f.write(str(result) + "\n")

    #f.close()
