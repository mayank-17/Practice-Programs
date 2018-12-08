def swap_case(s):
    a = ""
    for let in s:
        if let.isupper() == True:
            a+=(let.lower())
        else:
            a+=(let.upper())
    return a
string='helLoA'

str2=''

str2=swap_case(string)

print(str2)


a='hello you are'
c='k'
print(a[:5]+c+a[6:])