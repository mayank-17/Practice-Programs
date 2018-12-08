from numpy import array, sum

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))

    noDuplicatesA = list(set(A))
    less = 0
    less = sum(array(noDuplicatesA) <= N)

    print(N-less)