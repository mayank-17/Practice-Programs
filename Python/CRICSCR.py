n = int(input())
R, W = [], []
for i in range(n):
    r, w = map(int,input().split())
    R.append(r)
    W.append(w)
if R == sorted(R) and W == sorted(W):
    print("YES")
else:
    print("NO")