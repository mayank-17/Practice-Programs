from numpy import array

def nonZeroSub(List, N):
    count = 0
    result = 0
    for i in range(N):

        if count == 0:
            Min_i = 10
            Max_i = 0

        if List[i] <= 0:
            count = 0
        else:
            Min_i = min(Min_i, i)
            Max_i = max(Max_i, i)
            count += 1
            result = max(result, count)
    return List[Min_i:Max_i+1]
        
def removeCommon(List):
    noCommon = []
    for i in List:
        if i not in noCommon:
            noCommon.append(i)
    return (len(noCommon)-1)




        
N = int(input())
height = list(map(int, input().strip().split()))
myList = nonZeroSub(height,N)
print(removeCommon(myList))
