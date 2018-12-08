# from fractions import gcd
test = int(input())
def is_prime(candidate):
    for n in range(2, candidate):
        if candidate % n == 0:
            return False
    return True


def gcd(a, b):
    if (b == 0):
        return a
    else:
         return gcd(b, a % b)




yes, no = 0, 0
for i in range(test):
    n = int(input())
    myElements = list(map(int,input().split()))
    res = myElements[0]
    for c in myElements[1::]:
        res = gcd(res, c)

    for j in myElements:
        if (is_prime(j)):
            yes += 1
        else:
            no += 1
    if res == 1:
        print("0")
    elif (yes < n):
        print(no)
    elif res != 1:
        print("-1")



