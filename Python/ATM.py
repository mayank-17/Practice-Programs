for _ in range(int(input())):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    for i in A:
        if i <= K:
            print(1, end='')
            K = K - i
        else:
            print(0, end='')
    print()
