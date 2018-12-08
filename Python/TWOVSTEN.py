test = int(input())
for i in range(test):
    num = int(input())
    myList = list(str(num))
    if num%10 == 0:
        print("0") 
    elif (myList[-1] == '5') or (myList[-1] == '0'):
        count = 0
        while num%10 != 0:
            num=num*2
            count += 1
        print(count)
    elif (myList[-1] != '5') or (myList[-1] != '0'):
        print("-1")