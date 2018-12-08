test = int(input())
for i in range(test):
    robot = list(input())
    Length = len(robot)
    count = 0
    n,y =0,0
    for j in range(len(robot)):
        count += 1
        if robot[j] == 'S' and count < Length:
            n = 1
        else:
            y = 1
    if len("".join(set(robot))) == 1:
            y = 1
    if y == 1:
        print("yes")
    elif n == 1:
        print("no")    
        #elif robot[j]