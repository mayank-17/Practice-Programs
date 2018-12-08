def reverse(num):
    remainder, reverseOfNumber = 0,0
    while(num > 0):
        remainder = num  % 10
        num = num  // 10
        reverseOfNumber = reverseOfNumber * 10 + remainder
    return reverseOfNumber

num = int(input()) 
print(reverse(num))
       