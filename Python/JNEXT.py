test = int(input())
for i in range(test):
    N = int(input())
    A = list(map(int, input().split()))

    for j in range(N-1, -1, -1):
        if(A[j] > A[j-1]):
            break
    if (j == 0):
        print('-1')
    else:
    	for k in range(N-1, -1, -1):
            if(A[k] > A[j-1]):
                break

    	A[j-1], A[k] = A[k], A[j-1]

    	part1 = A[:j]
    	part2 = A[j:]

    	part2 = part2[::-1]

    	part1.extend(part2)
    	print("".join(str(i) for i in part1))
