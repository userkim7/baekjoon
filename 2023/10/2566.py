m=[*map(int,open(0).read().split())];print(m[i:=m.index(max(m))],i//9+1,i%9+1)

###탐색

####숏코딩 2위
m=open(0).read().split();print(m[i:=m.index(max(m,key=int))],i//9+1,i%9+1)
