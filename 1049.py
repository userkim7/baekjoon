N,M=map(int,input().split())
stores=[input().split() for _ in range(M)]
x=[int(store[0]) for store in stores]
y=[int(store[1]) for store in stores]
k=N//6
a=x+[i*6 for i in y]
if N%6:
    b=x+[i*(N%6) for i in y]
    print(min(a)*k+min(b))
else:
    print(min(a)*k)

###최솟값
