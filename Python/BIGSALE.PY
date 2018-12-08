t=int(input())
for i in range(t):
    n=int(input())
    loss=0.0
    for j in range(n):
        dis,pro=0.0,0.0
        rep=list(map(float,input().split()))
        pro=((rep[0]*rep[2])/100)+rep[0]
        dis=(pro*rep[2])/100
        loss+=(rep[0]-abs(pro-dis))*rep[1]
    print(loss)
