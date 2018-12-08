def descending(ls):
    for i in range (len(ls)-1):
        temp = False
        if(ls[i] >= ls[i+1]):
            temp = True
        else:
            temp = False
            break
    return temp

ls = list(input())
print(ls)
