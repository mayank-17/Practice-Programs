test = int(input())
for j in range(test):
    one,two,three,cone,ctwo,cthree=[],[],[],[],[],[]
    num = int(input())
    mylist=[]
    for i in range(num):
        mylist.append(list(map(int,input().split())))
    for k in range(len(mylist)):
        if mylist[k][1] == 1:
            one.append(mylist[k][2])
            cone.append(mylist[k][0])
        if mylist[k][1] == 2:
            two.append(mylist[k][2])
            ctwo.append(mylist[k][0])
        if mylist[k][1] == 3:
            three.append(mylist[k][2])
            cthree.append(mylist[k][0])
    maxDone=max(one)
    l1=one.index(maxDone)
    c1=cone[l1]
    maxDtwo=max(two)
    l2=two.index(maxDtwo)
    print(l2)
    c2=ctwo[l2]
    maxDthree=max(three)
    count3 = three.count(maxDthree)
    for i, n in enumerate(three):
        if n == maxDthree:
            print(i,n)
    l3=three.index(maxDthree)
    c3=cthree[l3]
    print(maxDone,c1)
    print(maxDtwo,c2)
    print(maxDthree,c3)           