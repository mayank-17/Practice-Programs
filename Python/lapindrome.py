test=int(input())
for i in range(test):
	string=input()
	if len(string)%2==0:
		be=len(string)//2
		firsthalf=string[0:be]
		sechalf=string[be:len(string)]
	else :
		bo=(len(string)-1)//2
		firsthalf=string[0:bo]
		sechalf=string[bo+1:len(string)]
	firsthalf,sechalf=list(firsthalf),list(sechalf)
	lapin=0
	for i in range(len(firsthalf)):
		if firsthalf[i] in sechalf:
			if firsthalf.count(firsthalf[i]) == sechalf.count(firsthalf[i]):
				lapin=1
			else :
				lapin=0
				break
		else:
			lapin=0
			break
	if lapin == 1 :
		print("YES")
	else :
		print("NO")