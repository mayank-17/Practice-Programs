def simplestSum(k, a, b):
    sum2=0
    for i in range(a,b+1):
        j=1
        sum1=0
        while j<=i:
            sum1=sum1+j
            j=j*k
            j+=1
        sum2=sum2+sum1
    return sum2%(10**9 + 7)

if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        k, a, b = input().strip().split(' ')
        k, a, b = [int(k), int(a), int(b)]
        result = simplestSum(k, a, b)
        print(result)
