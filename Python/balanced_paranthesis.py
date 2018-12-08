# exp=list(input())
# p1 = [i for i, x in enumerate(exp) if x == "{"]
# p2 = [i for i, x in enumerate(exp) if x == "}"]
# p3 = [i for i, x in enumerate(exp) if x == "("]
# p4 = [i for i, x in enumerate(exp) if x == ")"]
# if len(p1) == len(p2):
# 	b=1
# 	if len(p3) == len(p4):
# 		b=1
# 	else:
# 		b=0
# else:
# 	b=0

# print(b)

for t in range(int(input())):
    s = input()
    stk = 0
    i, j = 0, 0
    if s[0] == ">":
        print(0)
        continue
    for i in range(len(s)):
        if s[i] == "<":
            stk += 1
        elif s[i] == ">":
            if stk == 0:
                break
            stk -= 1

        if stk == 0:
            j = i
    if j == 0:
        print(j)
    else:
        print(j+1)