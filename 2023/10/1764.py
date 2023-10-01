n,m=map(int,input().split())
a=set([input()for _ in'0'*n])
b=set([input()for _ in'0'*m])
print(len(a&b),*sorted(a&b),sep='\n')

###집합
