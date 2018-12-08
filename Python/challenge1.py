for i in range(1,5):
	print(i)


n = int(input().strip())
dict1={}
for a0 in range(n):
    name, d, j = input().strip().split(' ')
    name, d, j = [str(name), int(d), int(j)]
    dict1[name]=j-d
for name,diff in dict1.items():
    if diff==max(dict1.values()):
	    print(name,max(dict1.values()))
	    break
