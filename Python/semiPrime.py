import math 

def checkSemiprime(num): 
    cnt = 0
  
    for i in range(2, int(math.sqrt(num)) + 1): 
        while num % i == 0: 
            num /= i 
            cnt += 1 
        if cnt >= 2:  
            break

    if(num > 1): 
        cnt += 1
 
    return cnt == 2
  
def semiprime(n): 
    if checkSemiprime(n) == True: 
        return True 
    else: 
        return False 

def isPerfectSquare(x): 
    sr = math.sqrt(x) 
    return ((sr - math.floor(sr)) == 0)
def binarySearch(arr, l, r, x): 
  
    while l <= r: 
  
        mid = int(l + (r - l)/2) 

        if arr[mid] == x: 
            return mid 

        elif arr[mid] < x: 
            l = mid + 1

        else: 
            r = mid - 1

    return -1

SP = []

for i in range(1, 200):
    if isPerfectSquare(i):
        pass
    else:
        if (semiprime(i) == True):
            SP.append(i)

SUM_OF_SEMIPRIMES = []

for i in range(len(SP)):
    for j in range(len(SP)):
        if SP[i] + SP[j] <= 200 and SP[i] + SP[j] not in SUM_OF_SEMIPRIMES:
            SUM_OF_SEMIPRIMES.append(SP[i] + SP[j])

SUM_OF_SEMIPRIMES = sorted(SUM_OF_SEMIPRIMES)
print(len(SUM_OF_SEMIPRIMES))

def main():
    for _ in range(int(input())):
        N = int(input())
        if binarySearch(SUM_OF_SEMIPRIMES, 0, len(SUM_OF_SEMIPRIMES) - 1, N) != -1:
            print("YES")
        else:
            print("NO")

main()
