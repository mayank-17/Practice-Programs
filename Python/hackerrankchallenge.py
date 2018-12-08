def maximumPeople(p, x, y, r):
    pop=sum(p)
    c=0
    for i,j in zip(y,r):
        if int(j)+int(i) in x or int(j)-int(i) in x:
            c=c+1
    if len(r)>1:
        r.pop(max(r))
        c=c-1
        
    else:
        return pop
    


if __name__ == "__main__":
    n = int(input().strip())
    p = list(map(int, input().strip().split(' ')))
    x = list(map(int, input().strip().split(' ')))
    m = int(input().strip())
    y = list(map(int, input().strip().split(' ')))
    r = list(map(int, input().strip().split(' ')))
    result = maximumPeople(p, x, y, r)
    print(result)
