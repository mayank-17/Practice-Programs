'''
def genPrime(r):
    myList = []
    for a in range(2, r+1):
        k = 0
        for i in range(2, a//2+1):
            if(a % i == 0):
                k = k+1
        if(k <= 0):
            myList.append(a)
    return myList


test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    myPrimeList = genPrime(n)
    if n-m in myPrimeList:
        print("YES")
    else:
        print("NO")

'''
from fractions import gcd
test = int(input())
for i in range(test):
    n, m = map(int, input().split())
    count = 0
    myList = []
    j = n+1
    while(count != m):
        if gcd(n, j) == 2:
            count += 1
            myList.append(j)
        j += 1
    [print(i, end=' ') for i in myList]
    print()
