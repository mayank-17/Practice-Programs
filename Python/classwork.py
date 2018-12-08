# radius = eval(input("Enter radius:"))
# area = (radius ** 2) * 3.14159
# print("The area for the circle of radius", radius, "is", area)
# print(int(5.9999999))

# a = input("Enter the value:")

# def evenOrOdd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# num = int(input("Enter the number please!"))
# print(evenOrOdd(num))

# a = [6, 2, 9, 1, 2, 8, 13]
# num = int(input("Choose a number:"))
# lessThan10 = [i for i in a if i < num]

# print(lessThan10)

# import keyword
# print(keyword.kwlist)

# a,b,c = int(input()),input(),float(input())

# a,b,c =input("enter the 3 no.").split(",")
# print(a,b,c)
# a1=eval(a)
# b1=eval(b)
# c1=eval(c)
# avg=(a1+b1+c1)/3
# print(avg)

# import math

# # x, y, z = -25, 11, 5.7701

# # math.sqrt(x)

# from math import pi
# print(math.pi)

# angleInRadians = 0.7853981633974483

# angleInDegree = math.degrees(angleInRadians)

# print(angleInDegree)

# import math
# def count(arr, x, n):

#     i = first(arr, 0, n-1, x, n)

#     if i == -1:
#         return i

#     j = last(arr, i, n-1, x, n)     

#     return j-i+1

# def first(arr, low, high, x, n):
#     if high >= low:
#         mid = (low + high)//2     
         
#     if (mid == 0 or x > arr[mid-1]) and arr[mid] == x:
#         return mid
#     elif x > arr[mid]:
#         return first(arr, (mid + 1), high, x, n)
#     else:
#         return first(arr, low, (mid -1), x, n)
#     return -1

# def last(arr, low, high, x, n):
#     if high >= low:
#         mid = (low + high)//2 
  
#     if(mid == n-1 or x < arr[mid+1]) and arr[mid] == x :
#         return mid
#     elif x < arr[mid]:
#         return last(arr, low, (mid -1), x, n)
#     else:
#         return last(arr, (mid + 1), high, x, n)     
#     return -1

# def calAreaPoly(myDict):
#     ans = 0
#     myDict2 = {}
#     for key, value in myDict.items():
#         ans = ((value * key) ** 2) / (4 * math.tan(180/value))
#         # print(key,value,ans)
#         myDict2[ans] = [key, value]
#     return myDict2

# def checkPoly(sticks, n):
#     canBePoly = {}
#     sticks = sorted(sticks)
#     unique = list(set(sticks))
#     for i in unique:
#         c = count(sticks, i, n)
#         if c >= 3:
#             canBePoly[i] = c
#     myDict = calAreaPoly(canBePoly)
#     greatest = sorted(myDict.keys())[-1]
#     c = myDict[greatest]
#     c = c[1]
#     return c
    
# num = int(input())
# sticks = list(map(int, input().split()))
# print(checkPoly(sticks, num))

# listOfNumbers = list(map(int, input().split()))
# print(list(set(listOfNumbers)))
# noDuplicates = []
# for i in listOfNumbers:
#     if i not in noDuplicates:
#         noDuplicates.append(i)
    
# print(noDuplicates)

# big_num_1 = 1000
# big_num_2 = 1000

# small_num_1 = 1
# small_num_2 = 1

# print(big_num_1 is big_num_2)
# print(small_num_1 is small_num_2)

################################################# LOOPS ##########################################

# print("Hello Python \n" * 3)

# i = 1

# def func():
#     # i = 2
#     print(i, "in func()")

# print(i, 'global')

# func()

# print(globals())
# print(locals())

# glob = 1
# def foo():
#     loc = 5
#     print('loc in foo(): ', 'loc' in locals())

# foo()

# print('loc in global: ', 'loc' in globals())
# print('glob in global: ', 'foo' in globals())


# a_var = 'global value'

# def outer():
#     # a_var = 'enclosed value'

#     def inner():
#         # a_var = 'local value'
#         print(a_var)

#     inner()
# outer()

############################ LEGB - Local, Enclosed, Global, Built-in ##########################################
""" 
a_var = 'global variable'

def len(in_var):
    print('called my len() function')
    l = 0
    for _ in in_var:
        l += 1
    return l

def a_func(in_var):
    len_in_var = len(in_var)
    print('Input variable is of length', len_in_var)

a_func('Hello, World!') """

# a = [1,2,3]
# b = [4,5,6]

# for i, j in zip(a, b):
#     print(j-i)




'''

def calculateVariables(annualInterestRate, numberOfYears, loanAmount):
    annualInterestRate = int(annualInterestRate[:len(annualInterestRate)-1])
    
    return annualInterestRate, numberOfYears, loanAmount

def calculateMonthlyInterestRate(annualInterestRate):
    monthlyInterestRate = annualInterestRate / 1200
    return monthlyInterestRate

def monthlyPayment(loanAmount, numberOfYears, annualInterestRate):
    monthlyInterestRate = calculateMonthlyInterestRate(annualInterestRate)
    calculatedMonthlyPayment = (loanAmount * monthlyInterestRate) / (1 - (1 / (1 + (monthlyInterestRate ** (numberOfYears*12)))))
    return calculatedMonthlyPayment

def totalPayment(numberOfYears, loanAmount, annualInterestRate):
    calculatedMonthlyPayment = monthlyPayment(loanAmount, numberOfYears, annualInterestRate)
    calculatedTotalPayment = calculatedMonthlyPayment * numberOfYears * 12
    return calculatedTotalPayment

def displayDetails(loanAmount, numberOfYears, annualInterestRate):
    calculatedMonthlyPayment = monthlyPayment(loanAmount, numberOfYears, annualInterestRate)
    calculatedTotalPayment = totalPayment(numberOfYears, loanAmount, annualInterestRate)
    print("Here are your results :-)")
    print("The Monthly Payment sums to be :", calculatedMonthlyPayment)
    print("The Total Payment amounts to :", calculatedTotalPayment)

## Inputs
annualInterestRate = input("Please enter the annual rate: ")
numberOfYears = eval(input("Please enter No. of Years: "))
print("This is the last input :-)")
loanAmount = eval(input("Please enter Loan Amount: "))

annualInterestRate, numberOfYears, loanAmount = calculateVariables(annualInterestRate, numberOfYears, loanAmount)

calculateMonthlyInterestRate(annualInterestRate)

monthlyPayment(loanAmount, numberOfYears, annualInterestRate)

totalPayment(numberOfYears, loanAmount, annualInterestRate)

displayDetails(loanAmount, numberOfYears, annualInterestRate)

'''


# N = int(input())
# word = list(input())

# def checkIsPalindrome(word):
#     length = len(word)

#     start = 0
#     end = start + length - 1

#     while (end > start):
#         if (end != start):
#             return False
#         end -= 1
#         start += 1
    
#     return True

# def noOfAppend(word):
#     if checkIsPalindrome(word):
#         print(word)
    
# day = 0
# myList = list(range(1, 32, 2))
# set1 = set(myList)
# print("Is your birthday in this set? Answer Y for Yes and N for No.", list(set1))

# answer = input()
# if (answer == 'Y' or answer == 'y'):
#     day += 1



# myList2 = []
# count = 0
# for i in range(2, 32, 2):
#     if count == 0:
#         myList2.append(i)
#         myList2.append(i+1)
#         count += 1
#     else:
#         count -= 1
#         continue

# set2 = list(myList2)
# print("Is your birthday in this set? Answer Y for Yes and N for No.", set2)
# answer = input()
# if (answer == 'Y' or answer == 'y'):
#     day += 2

# myList3 = []
# count = 0
# for i in range(4, 32, 4):
#     if count == 0:
#         for j in range(i, i+4):
#             myList3.append(j)
#         count += 1
#     else:
#         count -= 1
#         continue

# set3 = list(myList3)
# print("Is your birthday in this set? Answer Y for Yes and N for No.", set3)
# answer = input()
# if (answer == 'Y' or answer == 'y'):
#     day += 4

# myList4 = []
# count = 0
# for i in range(8, 32, 8):
#     if count == 0:
#         for j in range(i, i+8):
#             myList4.append(j)
#         count += 1
#     else:
#         count -= 1
#         continue

# set4 = list(myList4)
# print("Is your birthday in this set? Answer Y for Yes and N for No.", set4)
# answer = input()
# if (answer == 'Y' or answer == 'y'):
#     day += 8

# myList5 = []
# count = 0
# for i in range(16, 32, 16):
#     if count == 0:
#         for j in range(i, i+16+1):
#             myList5.append(j)
#         count += 1
#     else:
#         count -= 1
#         continue

# set5 = list(myList5)
# print("Is your birthday in this set? Answer Y for Yes and N for No.", set5)
# answer = input()
# if (answer == 'Y' or answer == 'y'):
#     day += 16

# print("Good news for you, I have just guessed your birthday!!", day)

# import time
# score = int(input("Enter your score:"))

# tic = time.time()
# answer = 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'
# toc = time.time()
# print("Grade is:", answer, "time taken for First", 1000 * (toc-tic), "ms")

# score = int(input("Enter your score:"))

# tic = time.time()
# if score >= 90:
#     answer = 'A'
# else:
#     if score >= 80:
#         answer = 'B' 
#     else: 
#         if score >= 70:
#             answer = 'C' 
#         else:
#             if score >= 60:
#                 answer = 'D'
#             else:
#                 answer = 'F'
# toc = time.time()
# print("Grade is:", answer, "time taken for Second", 1000 * (toc-tic), "ms")


# height = eval(input("Enter height: "))
# weight = eval(input("Enter weight: "))

# bmi = weight / (height) ** 2

# interpretation = 'Underweight' if bmi < 18.5 else 'Normal' if bmi >= 18.5 and bmi <= 24.9 else 'Overweight' if bmi >= 25.0 and bmi <= 29.9 else 'Obese'

# print(interpretation)
# myList = []
# tic = time.time()
# for i in range (1,10001):
#     myList.append(i)
# toc = time.time()

# print("Normal for: ", 1000 * (toc-tic), "ms")
# myList = []
# tic = time.time()
# myList = [i for i in range(1, 10001)]
# toc = time.time()

# print("Comprehension for: ", 1000 * (toc-tic), "ms")

# month = int(input("Enter month please :-) "))
# year = int(input("Enter year please :-) "))

# monthList = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
# monthList = {1:(31,'January'), 2:(28, 'February'), 3:(31, 'March'), 4:(30, 'April'), 5:(31, 'May'), 6:(30, 'June'), 7:(31, 'July'),8:(31, 'August'), 9:(30, 'September'), 10:(31, 'October'), 11:(30, 'November'), 12:(31, 'December')}
# def is_leap(year):
#     leap = False
#     if year%4 == 0:
#         leap = True
#         if year%100 == 0:
#             leap = False
#             if year%400 == 0:
#                 leap = True
#     return leap

# def calculateDays(monthList, year, month):
#     if month == 2:
#         if is_leap(year) == True:
#             print("There are {} days in {} of year {}".format(monthList[month][0] + 1, monthList[month][1], year))
#         else:
#             print("There are {} days in {} of year {}".format(monthList[month][0], monthList[month][1], year))
#     else:
#         print("There are {} days in {} of year {}".format(monthList[month][0], monthList[month][1], year))

# calculateDays(monthList, year, month)

######################### Even Odd ######################
# series = list(map(int, input("Enter numbers: ").split()))
# print("Even:", sum(1 for i in series if i % 2 == 0), "Odd:", sum(1 for i in series if i % 2 != 0))

################### Three Five ############################
# [print(("Three"*(i%3 == 0) + "Five"*(i%5 == 0)) or i) for i in range(1, 51)] 

################## 3 or 6 ##################

# [print(i) for i in range(0, 7) if i not in [3, 6]]

############# GCD ##############

# def calGCD(num1, num2):
#     k, gcd = 2, 1
#     while k <= num1 or k <= num2:
#         if ((num1 % k == 0) and (num2 % k == 0)):
#             gcd = k
#         k += 1
#     return gcd

# def funcGCD(num1, num2):
#     while num2:
#         num1, num2 = num2, num1 % num2
#     return num1

# a, b = map(int, input("Enter two numbers: ").split())
# print("GCD is : ", calGCD(a, b))
# print("GCD is : ", funcGCD(a, b))

#################################### Guessing Numbers ###########################

# def binarySearch (arr, l, r, x): 
#     if r >= l: 
#         mid = l + (r - l)/2
#         if arr[mid] == x: 
#             return mid 

#         elif arr[mid] > x: 
#             return binarySearch(arr, l, mid-1, x) 

#         else: 
#             return binarySearch(arr, mid+1, r, x) 

# from random import randint
# print("Guess a magic number b/w 0 and 100 \nEnter your guess: ")
# guess = int(input())
# comp = randint(0, 100)
# count = 1
# while guess != comp:
#     print("Your guess is too high" * (guess > comp) + "Your guess is too low" * (guess < comp))
#     guess = int(input("Enter your guess: "))
#     count += 1
# print("You have got it correct in {} chances.". format(count))
    
################################################## Let's Play Lottery ##################################################
# from random import randint

# print("Let's Play Lottery")
# print("Enter a two digit number please: ")

# myNum = input()
# myRandom = str(randint(10, 100))

# print("Hurray! You won $10,000!" if (myNum[0] == myRandom[0] and myNum[1] == myRandom[1]) else "Congrats! You won $3,000!" if (myNum[0] == myRandom[1] and myNum[1] == myRandom[0]) else "Wow! You won $1,000!" if (myNum[0] in myRandom or myNum[1] in myRandom) else "Better luck next time!")

# if (myNum[0] == myRandom[0] and myNum[1] == myRandom[1]):
#     print("Hurray! You won $10,000!")
# elif (myNum[0] == myRandom[1] and myNum[1] == myRandom[0]):
#     print("Congrats! You won $3,000!")
# elif (myNum[0] in myRandom or myNum[1] in myRandom):
#     print("Wow! You won $1,000!")
# else:
#     print("Better luck next time!")


##################################################### Lambda #######################################

# def factorial(num):
#     fact = 1
#     for i in range(num, 0, -1):
#         fact *= i
#     return fact

# print(factorial(5))

# from functools import reduce
# print("The factorial is : {}".format(reduce(lambda x, y: x*y, range(1, int(input("Enter a number: ")) + 1))))

# print(*range(5))

################################################# Angles of triangle ######################################################

# import math

# x1, y1 = map(float, input().split())
# x2, y2 = map(float, input().split())
# x3, y3 = map(float, input().split())

# def euclideanDistance(a, b, c, d):
#     dist = math.sqrt( (c-a) ** 2 + (d-b) ** 2)
#     return dist

# def calculateDistances(x1, x2, x3, y1, y2, y3):
#     a = euclideanDistance(x2, y2, x3, y3)
#     b = euclideanDistance(x1, y1, x2, y2)
#     c = euclideanDistance(x3, y3, x1, y1)
#     return a, b, c

# def calculateAngles(x1, x2, x3, y1, y2, y3):
#     a, b, c = calculateDistances(x1, x2, x3, y1, y2, y3)

#     A = math.acos(((a * a) - (b * b) - (c * c)) / (-2 * b * c))
#     B = math.acos(((b * b) - (a * a) - (c * c)) / (-2 * a * c))
#     C = math.acos(((c * c) - (b * b) - (a * a)) / (-2 * a * b))
#     return A, B, C

# def main():
#     A, B, C = calculateAngles(x1, x2, x3, y1, y2, y3)
#     print("Angle A is : {} degrees, B is : {} degrees, C is : {} degrees".format(round(math.degrees(A)), round(math.degrees(B)), round(math.degrees(C))))

# main()

##################################################################################################################################################################

# import turtle

# turtle.pensize(3)
# turtle.color("red")
# turtle.penup()
# turtle.goto(-200, -50)
# turtle.pendown()
# turtle.fillcolor("red")
# turtle.begin_fill()
# turtle.circle(40, steps = 3)
# turtle.end_fill()

# turtle.color("yellow")
# turtle.penup()
# turtle.goto(-120, -60)
# turtle.pendown()
# turtle.fillcolor("yellow")
# turtle.begin_fill()
# turtle.circle(40, steps=4)
# turtle.end_fill()

# turtle.color("blue")
# turtle.penup()
# turtle.goto(-30, -60)
# turtle.pendown()
# turtle.fillcolor("blue")
# turtle.begin_fill()
# turtle.circle(40, steps=5)
# turtle.end_fill()

# turtle.color("green")
# turtle.penup()
# turtle.goto(60, -60)
# turtle.pendown()
# turtle.fillcolor("green")
# turtle.begin_fill()
# turtle.circle(40, steps=6)
# turtle.end_fill()

# turtle.color("pink")
# turtle.penup()
# turtle.goto(160, -60)
# turtle.pendown()
# turtle.fillcolor("pink")
# turtle.begin_fill()
# turtle.circle(40)
# turtle.end_fill()

########################################################################## Format ###############################################################

# print(format(57.453773829920, '.2f'))

################################################################# Sets, Lists, Dictionaries, Tuple #############################################

############################################################## Checking #############################################################

# print("Checking comparision")

# numbers = 10000

# myList = list(range(10001))
# # print(myList)
# mySet = set(range(10001))
# # print(mySet)
# import time
# import random
# random.shuffle(myList)

# # For list
# tic = time.time()

# for i in range(10001):
#     if i in myList:
#         pass

# toc = time.time()

# print("Time taken by list is: ", (toc-tic), " seconds")

# # For set

# tic = time.time()

# for i in mySet:
#     if i in mySet:
#         pass

# toc = time.time()

# print("Time taken by set is: ", (toc-tic), " seconds")

##################################################################### Remove ###################################################

# print("Removing comparision")

# numbers = 10000

# myList = list(range(10001))
# # print(myList)
# mySet = set(range(10001))
# # print(mySet)
# import time
# import random
# random.shuffle(myList)

# # For list
# tic = time.time()

# for i in range(10001):
#     myList.remove(i)

# toc = time.time()

# print("Time taken by list is: ", (toc-tic), " seconds")

# # For set

# tic = time.time()

# for i in range(10001):
#     mySet.remove(i)

# toc = time.time()

# print("Time taken by set is: ", (toc-tic), " seconds")

####################################################################### Dictionaries ########################################################

# def processLine(line, wordCounts):
#     line = replacePunctuation(line)

#     words = line.split()

#     for word in words:
#         if word in wordCounts:
#             wordCounts[word] += 1
#         else:
#             wordCounts[word] = 1

# def replacePunctuation(line):
#     punc = list("~@#$%^&*(\)_+!}{|:?> <'[];,./-=")
#     for ch in line:
#         if ch in punc:
#             line = line.replace(ch, " ")
#     return line

# def main():
#     filename = input("Enter a filename: ")
#     infile = open(filename, 'r')

#     wordCounts = dict()

#     for line in infile:
#         processLine(line.lower(), wordCounts)
    
#     pairs = list(wordCounts.items())

#     print(pairs)

#     items = [[x, y] for (y, x) in pairs]

#     items.sort()

#     print("Words", "\t\t", "Counts")
#     print()
#     Words, Counts = [], []
#     for i in range(len(items) - 1, len(items) - 11, -1):
#         # print(Words.append(items[i][1]), Counts.append(items[i][0]))

#     for i in range(len(Words)):
#         print(Words[i], '\t', Counts[i])
# main()

####################################################################################################################################
# import numpy as np

# def sumOfList(myList):
#     return np.sum(myList)

# def productOfList(myList):
#     return np.prod(myList)

# def getLargest(myList):
#     return myList.max()

# def getSmallest(myList):
#     return myList.min()

# def main():
#     myList = list(map(int, input("Enter List: ").split()))
#     myList = np.array(myList)
#     print("The sum of List is: ", sumOfList(myList))
#     print("The product of List is: ", productOfList(myList))
#     print("Maximum element of List is: ", getLargest(myList))
#     print("Minimum element of List is: ", getSmallest(myList))

# main()


################################################################################## Reverse List ####################################################################################

# myList = list(map(str, input("Enter List: ").split()))

# def reverse(myList):
#     for i in range(len(myList) // 2):
#         myList[i], myList[len(myList) - i - 1] = myList[len(myList) - i - 1], myList[i]
#     return myList

# print("The reverse of list is: ", reverse(myList))

#######################################################################################################################################################################################

# def toFindUpperAndLowerCaseCount(string):
    
#     myDictOfUpperandLowerCase = dict()

#     countUpper, countLower = 0, 0
#     for i in string:
#         if (i.isupper()):
#             countUpper += 1
#         elif (i.islower()):
#             countLower += 1
#     myDictOfUpperandLowerCase["Upper Case Counts are : "] = countUpper
#     myDictOfUpperandLowerCase["Lower Case Counts are : "] = countLower

#     return myDictOfUpperandLowerCase

# def main():

#     string = input("Enter the string: ")

#     print(toFindUpperAndLowerCaseCount(string))

# main()

####################################################################################################################################################################################

# def toCheck(myList1, myList2):
#     for i in range(len(myList1)):
#         for j in range(len(myList2)):
#             if myList1[i] == myList2[j]:
#                 return True
#     return False

# def main():
#     myList1, myList2 = list(map(int, input("Enter the first list: ").split())), list(map(int, input("Enter the second list: ").split()))

#     print("Matched" * (toCheck(myList1, myList2) == True) + "No Match" * (toCheck(myList1, myList2) == False))

# main()

    
######################################################################################################################################################################################

# Series 1/1! + 4/2! + 27/3! + ...........

# def fact(n):
#     if (n == 1 or n == 0):
#         return 1
#     return n * fact(n-1)

# def series(n):
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i**i / fact(i)
#     return sum

# print(series(5))

#######################################################################################################################################################################################

# def toPrint(rows, col, sym):
#     for _ in range(cols):
#         print(sym*rows)

# sym = input("Enter symbol: ")
# rows = int(input("Enter rows: "))
# cols = int(input("Enter columns: "))

# toPrint(rows, cols, sym)

############################################################################### FILE HANDLING ##########################################################################################

# f = open("demo.txt")
# print(f.read())
# f.close()

# file = open("file.txt", "wb")
# print("Name of the file: ", file.name)
# print("Is the file closed: ", file.closed)
# print("File has been opened in: ", file.name)


# file = open("D:\Programming\Practice Programs\Python\Programs\File3.txt", "rb")
# print("Position of file pointer before reading is: ", file.tell())
# print(file.read(5))
# print("Position of file pointer before reading is: ", file.tell())
# print("Setting 5 bytes from the current position of the file pointer")
# file.seek(5, 1)
# print(file.read())
# file.close()

# numbers = '0123456789'
# with open("D:\Programming\Practice Programs\Python\Programs\File3.txt", "rb") as f1, open("D:\Programming\Practice Programs\Python\Programs\File4.txt", "wb") as f2:
#     l = len(f1.read())
#     f1 = open("D:\Programming\Practice Programs\Python\Programs\File3.txt", "rb")
#     for i in range(l):
#         word = f1.read(1)
#         if (word in numbers.encode('ascii')):
#             continue
#         else:
#             f2.write(word)




# with open("D:\Programming\Practice Programs\Python\Programs\script1.py", "rb") as s1, open("D:\Programming\Practice Programs\Python\Programs\script2.py", "wb") as s2:
#     for line in s1:
#         if "'''".encode("ascii") in line or '#'.encode("ascii") in line or '"""'.encode("ascii") in line:
#             continue
#         else:
#             s2.write(line)

# with open("D:\Programming\Practice Programs\Python\Programs\script1.py", "r") as f1, open("D:\Programming\Practice Programs\Python\Programs\script2.py", "w") as f2:
#     content = f1.read()
#     f2.write(content.upper())


# class Students:
#     def __init__(self, name):
#         self.name = name
#         self.marks = []
#         print(__name__)
#     def __enterMarks(self):
#         for i in range(5):
#             m = int(input("Enter Marks of %s in subject %d: " %(self.name, i + 1)))
#             self.marks.append(m)
#     def display(self):
#         print(self.name, "got", self.marks)

# s1 = Students("Mayank")
# s1._Students__enterMarks()

class Base1:
    def __init__(self):
        print("Base 1 Class")
        super(Base1, self).__init__()

class Base2:
    def __init__(self):
        print("Base 2 Class")

class Derived(Base1, Base2):
    def __init__(self):
        super(Derived, self).__init__()
        print("Derived Class")
D = Derived()