test = int(input())
names = [int(input()) for i in range (0,test)]
sub = 'chef'
sublist = []
for j in range ( 0, len(sub) ):
    for k in range( j, len(sub)):
        if len(sub[j:k]) >= 2:
            sublist.append(sub[j:k])
count = 0
for i in names:
    for j in sublist:
        if j in i:
            count +=1
