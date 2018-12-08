def find_gcd(x, y):
     
    while(y):
        x, y = y, x % y
     
    return x
test = int(input())
n, k = map(int,input().split())
myElements = list(map(int,input().split()))
nums = []
for i in range(k):
    nums.append(i+1)
num1 = myElements[0]
num2 = myElements[1]
gcd = find_gcd(num1, num2)
 
for i in range(2, len(myElements)):
    gcd = find_gcd(gcd, myElements[i])
from numpy import array
def Cal(myElements):
    num1 = myElements[0]
    num2 = myElements[1]
    gcd = find_gcd(num1, num2)
    for i in range(2, len(myElements)):
        gcd = find_gcd(gcd, myElements[i])
    if gcd != 1:
        myElements = list(array(myElements)/i)
        Cal(myElements)
    return gcd

if Cal(myElements) != 1:
    print("YES")
else:
    print("NO")

    