from math import log, exp
# import sys
def fast_power(base, power):
    A = power * log(base)
    try:
        ans = exp(A)
    except OverflowError:
        ans = float('inf')
    return ans
    
test = int(input())
for i in range(test):
    a, b, n = map(int, input().split())
    a, b = abs(a), abs(b)
    if(fast_power(a, n) > fast_power(b, n)):

        print('1')
    elif(fast_power(a, n) < fast_power(b, n)):
        # print(fast_power(a, n), fast_power(b, n))
        print('2')
    else:
        print('0')
