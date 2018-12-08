# for _ in range(int(input())):
#     number = int(input())
#     number += 1
#     listNum = list(str(number))
#     count = listNum.count('3')
#     while count < 3 :
#         number += 1
#         listNum = list(str(number))
#         count = listNum.count('3')
        
#     print(number)

# [alice, bear, chalrton, daman]
# [alice, bear, chalrton, daman]
# [amir, bob, chalrton, daman]

# year = int(input())
# def isALeap(year):
#     leap = False
#     if year%4 == 0:
#         leap = True
#         if year%100 == 0:
#             leap = False
#             if year%400 == 0:
#                 leap = True
#     return leap

# if isALeap(year) == True:
#     print("Yes")
# else:
#     print("No")

integer = int(input())
if integer % 2 != 0 :
    print("Weird")
else:
    if integer >= 0 and integer <= 20:
        print("Not Weird")
    elif integer >= 21 and integer <= 25:
        print("Weird")
    elif integer > 25:
        print("Not Weird")