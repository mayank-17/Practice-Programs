test=int(input())
for i in range(test):
    n=int(input())
    colors=list(map(int,input().split()))
    for k in range(len(colors)):
        x=colors.count(colors[k])
        for j in range(x-1):
            maximum=max(colors)
            minimum=min(colors)
            z=colors.index(minimum)
            y=colors.index(maximum)
            if colors.count(minimum) == 1:
                pass
            else:
                colors[y]+=minimum
            if colors.count(maximum) == 1:
                pass
            else:
                colors[z]+=maximum

        
        

'''words = [w.replace('[br]', '<br />',) for w in colors]
                c_str=c_str.replace(i,i+i,j)
                colors=list(c_str)
                print(colors)
        if x == 1:
            c.append(0)
    print(c)
    print(sum(c)//2)'''