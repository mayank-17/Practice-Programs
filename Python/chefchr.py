def contiguous_substrings(string):
    str1=list("chef")
    c=0
    a=0
    for i in string:
        if i in str1:
            a=a+1
        if a == 4:
            c=c+1
        if a > 4:
            for i in reversed (string):
                contiguous_substrings(string)
                
                    
                
        if i not in str1:
            a=0
            
        
    return c        
t=int(input())
while t>0:
    str1=list(input())
    print(int(contiguous_substrings(str1)))
        
    t=t-1
