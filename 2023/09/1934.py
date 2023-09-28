def f(a,b,n):
 if not a%b==0!=print(int(n/b)):f(b,a%b,n)
exec(int(input())*"a,b=sorted(map(int,input().split()));f(b,a,a*b);")

###최소공배수,유클리드 호제법

####숏코딩 6위
import math
for n in[*open(0)][1:]:print(math.lcm(*map(int,n.split())))
