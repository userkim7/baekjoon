m,M=map(int,input().split())
s1=set(range(m,M+1))
s2=set()
num=2
while num**2<=M:
    s2.update(range((m//num**2+int(m%num**2!=0))*num**2,M+1,num**2))
    num+=1
print(len(s1-s2))
