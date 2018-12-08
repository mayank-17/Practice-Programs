def isPrime(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return 0
        else:
            return 1
    else:
        return 0

numOfElements = int(input())
queries = int(input())
myElements = list(map(int,input().split()))
for i in range(queries):
    Q  = list(map(int,input().split()))
    if Q[0] == 1:
        eleStartIndex = Q[1] - 1
        eleEndIndex = Q[2] - 1
        subElementsList = myElements[eleStartIndex:eleEndIndex+1]
        for j in range(len(subElementsList)):
            ele =subElementsList[j]
            ele -= 1
            while(ele >= 2):
                if isPrime(ele) == 1:
                    myElements[j + eleStartIndex] = myElements[j + eleStartIndex] - ele
                    break
                ele -= 1
    else:
        eleStartIndex = Q[1] - 1
        eleEndIndex = Q[2] - 1
        print(sum(myElements[eleStartIndex:eleEndIndex+1]))
