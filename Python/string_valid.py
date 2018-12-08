s = '123'
for i in s:
    if i.isalnum()==True:
        an=1            
    if i.isalpha()==True:
        a=1    
    if i.isdigit()==True:     
        d=1    
    if i.islower()==True:
        l=1    
    if i.isupper()==True:
        u=1      

if an==1:
    print("True")
else:
    print("False")
if a==1:
    print("True")
else:
    print("False")
if d==1:
    print("True")
else:
    print("False")
if l==1:
    print("True")
else:
    print("False")
if u==1:
    print("True")
else:
    print("False")
