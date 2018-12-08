import math
def count(arr, x, n):

    i = first(arr, 0, n-1, x, n)

    if i == -1:
        return i

    j = last(arr, i, n-1, x, n)     

    return j-i+1

def first(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2     
         
    if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
        return mid
    elif x > arr[mid]:
        return first(arr, (mid + 1), high, x, n)
    else:
        return first(arr, low, (mid -1), x, n)
    return -1

def last(arr, low, high, x, n):
    if high >= low:
        mid = (low + high)//2 
  
    if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
        return mid
    elif x < arr[mid]:
        return last(arr, low, (mid -1), x, n)
    else:
        return last(arr, (mid + 1), high, x, n)     
    return -1

def calAreaPoly(myDict):
    ans = 0
    myDict2 = {}
    for key, value in myDict.items():
        ans = ((value * key) ** 2) / (4 * math.tan(180/value))
        print(key,value,ans)
        myDict2[ans] = [key, value]
    return myDict2

def checkPoly(sticks, n):
    canBePoly = {}
    sticks = sorted(sticks)
    unique = list(set(sticks))
    for i in unique:
        c = count(sticks, i, n)
        if c >= 3:
            canBePoly[i] = c
        else:
            canBePoly[i] = NULL
    myDict = calAreaPoly(canBePoly)
    greatest = sorted(myDict.keys())[-1]
    c = myDict[greatest]
    c = c[1]
    return c
    
num = int(input())
sticks = list(map(int, input().split()))
print(checkPoly(sticks, num))