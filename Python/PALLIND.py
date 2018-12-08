'''m = 1000000007
x = 676
y = pow(x,m-2,m)
print(y)
'''
def modInverse(a, m) :
     
    g = gcd(a, m)
     
    if (g != 1) :
        print("Inverse doesn't exist")
         
    else :
         
        # If a and m are relatively prime,
        # then modulo inverse is a^(m-2) mode m
        return (power(a, m - 2, m))
     
# To compute x^y under modulo m
def power(x, y, m) :
     
    if (y == 0) :
        return 1
         
    p = power(x, y // 2, m) % m
    p = (p * p) % m
 
    if(y % 2 == 0) :
        return p 
    else : 
        return ((x * p) % m)
 
# Function to return gcd of a and b
def gcd(a, b) :
    if (a == 0) :
        return b
         
    return gcd(b % a, a)
     
 
# Driver Program
m = 1000000007
a = 26
print(modInverse(a, m))