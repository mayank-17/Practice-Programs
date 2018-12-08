from collections import deque
def get_all_substrings(string):
  length = len(string)
  alist = []
  for i in range(length):
    for j in range(i,length):
      alist.append(string[i:j + 1]) 
  return alist
x=[]
x=get_all_substrings('abcde')
d = deque(x)
d.rotate(-1)
print(d)

def rotations(num): 
    d = deque(num)
    rlist = []
    for i in xrange(len(d)):
        rlist.append(''.join(map(d.rotate(-1), d)))
    return set(rlist)

print (rotations('123')) 
print (rotations('111'))
print (rotations('197'))