# """import math
# # Complete the connectedCell function below.
# #def connectedCell(matrix):
# def connectedCell(matrix):
#     # Complete this function
#     result_list = []
#     n,m = len(matrix),len(matrix[0])
#     for i in range(0,n):
#         for j in range(0,m):
#             if matrix[i][j] == 1:
#                 result_list.append(dfs(matrix,i,j))
#     return max(result_list)
                
# def dfs(matrix,i,j):
#     n,m = len(matrix),len(matrix[0])
#     if i < 0 or j < 0 or i >= n or j >= m:
#         return 0
#     if matrix[i][j] == 0:
#         return 0
#     if matrix[i][j] == 1:
#         matrix[i][j] = 0
#         a,b,c,d = dfs(matrix,i-1,j),dfs(matrix,i+1,j),dfs(matrix,i,j-1),dfs(matrix,i,j+1)
#         if a == None:
#             a = 0
#         elif b == None:
#             b = 0
#         elif c == None:
#             c = 0
#         elif d == None:
#             d = 0
#         return 1+ a + b + c + d

# # n = int(input())

# # m = int(input())

# n,m = map(int,input().split())

# matrix = []

# for _ in range(n):
#     matrix.append(list(map(int, input().rstrip().split())))

# print(connectedCell(matrix))"""

# def count(S):
#     c = 1
#     for i in range(len(S)):
#         if(i < len(S)-1 and S[i+1] == S[i]):
#             S.delete(i)
#             i -= 1
#             c += 1
#         else:
#             S.insert(i+1, count)
#             count = 1
#             i += 1
#     return S

# test = int(input())
# R = []
# for i in range(test):
#     S = list(input())
#     letterSet = ('f','r','i','e','a')
#     for j in range(len(S)):
#         if S[j] in letterSet:
#             R.append('g')
#         else:
#             R.append('b')
#     print(R.count(S))

# def func(var):
#     return {1:'insert', 2:'update', 3:'modify'}[var]

# print(func(2))


def nextHigher(num):
    l = list(str(num))
    if(l == l[::-1]):
        return -1
    elif (l == sorted(l, reverse = True)):
        return -1
    strNum=str(num)
    length=len(strNum)
    for i in range(length-2, -1, -1):
        current=strNum[i]
        right=strNum[i+1]
        if current<right:
            temp=sorted(strNum[i:])
            # print(temp)
            next=temp[temp.index(current)+1]
            temp.remove(next)
            # print(temp)
            temp=''.join(temp)
            return int(strNum[:i]+next+temp)
    return num

test = int(input())
print(nextHigher(test))