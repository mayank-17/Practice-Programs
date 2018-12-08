#!/bin/python3

import sys

def howManyStudents(m, c):
    l=[]
    n=[]
    for i in range(m):
        l.append(i)

    for i in l:
    	n.append(c.count(i))

    return n   
        

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    c = list(map(int, input().strip().split(' ')))
    result = howManyStudents(m, c)
    print (" ".join(map(str, result)))


