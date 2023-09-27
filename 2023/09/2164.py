from collections import *
a=deque(range(int(input())))
while len(a)>1:del a[0];a.rotate(-1)
print(a[0]+1)

###데크
