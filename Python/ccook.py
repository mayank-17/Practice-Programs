n=int(input())

while n>0:
    p=input().split()
    print(p)
    count=0
    for i in p:
	    if i == '1':
		    count+=1

    if count == 0:
	    print("Beginner")
    elif count == 1:
        print("Junior Developer")
    elif count == 2:
        print("Middle Developer")
    elif count == 3:
        print("Senior Developer")        	
    elif count == 4:
       print("Hacker")
    elif count == 5:
       print("Jeff Dean")        

    n=n-1   