test = int(input())
for i in range(test):
    myString = input()
    myList = list(myString)
    count = 0
    myNumList = []
    for j in range(len(myString)):
        if myString[j].isdigit() == True:
            count+=1
            myNumList.append(myList[j])
    mySum = 0
    for k in myNumList:
        mySum = mySum + int(k)
    print(mySum)