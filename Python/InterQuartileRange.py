from statistics import median
Length = int(input())
Elements = list(map(int,input().split(" ")))
Frequency = list(map(int,input().split(" ")))
S = []
for i in range(len(Frequency)):
    count = Frequency[i]
    for j in range(count):
        S.append(Elements[i])
LB = len(S)//2
UB = len(S)
S = sorted(S)
S_lb = S[:LB]
if len(S) % 2 != 0:
    S_ub = S[LB+1:]
else:
    S_ub = S[LB:UB+1]
print('{0:.1f}'.format(median(S_ub) - median(S_lb)))