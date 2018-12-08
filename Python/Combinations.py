test = int(input())
for k in range(test):
    lt=list(input("Enter a String:"))
    a=len(lt)
    ll=lt[0:a]
    for i in range(0,a):
        for j in range(0,a-1):
            if(lt[i]==ll[j]):
                ll[j],ll[j+1]=ll[j+1],ll[j]
                if ll != lt:
                    print("".join(ll))
            else:
               continue