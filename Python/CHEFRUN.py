test = int(input())

for i in range(test):
    X1, X2, X3, V1, V2 = map(int,input().split())
    dis1 = X3 - X1
    # print(dis1)
    dis2 = X2 - X3
    # print(dis2)
    time1 = dis1/V1
    time2 = dis2/V2
    if (time1 < time2):
        print("Chef")
    elif (time2 < time1):
        print("Kefa")
    else:
        print("Draw")
