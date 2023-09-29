a,b=map(int,input().split())
c=range(1,a+1)
for i in range(a**b):
 for j in range(b):
  print(c[(i//a**(b-j-1))%a],end=' ')
 print()

###백트래킹
