def swap_case(s):
    str1=""
    for i in s:
        
        if i.isupper() == True:
            str1+=(i.lower())
        else:
            str1+=(i.upper())
    return str1
s='Hello'
String=''
String=swap_case(s)
print(String)
