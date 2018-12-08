'''N = int(input())
myList = []
for i in range(0,N):
    command = input().strip().split(" ")
    if command[0] == 'insert':
        myList.insert(int(command[1]),int(command[2]))
    if command[0] == 'print':
        print(myList)
'''
val = 75.000000000
#print('{0}'.format(val))
print('{0:.2f}'.format(val))
#print(val)