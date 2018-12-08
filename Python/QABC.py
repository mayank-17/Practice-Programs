for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    output = 0
    for i in range(0,N-1):
        DIFF = B[i] - A[i]
        if DIFF == 0:
            continue
        elif DIFF < 0:
            output = 0
            break
        else:
            while(DIFF > 0):
                B[i] -= 1
                B[i+1] -= 2
                B[i+2] -= 3
                DIFF -= 1
            # print(B)
    if B == A:
        output = 1
        # break
    else:
        output = 0
        # break
    print("TAK" * (output == 1) + "NIE" * (output == 0))