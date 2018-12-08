def count_substring(string,sub_string):
    s=0
    l=len(string)
    i=string.find(sub_string,s,l)
    
    if i!=-1:
        a=1
    else:
        a=0
    while i!=-1:
        i=string.find(sub_string,i+1,l)
        if i!=-1:
            a+=1
        else:
            break;    
    return a
ans=count_substring('birth','Birth')
print(ans)
