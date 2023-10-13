a=b=100
for i in[*open(0)][1:]:m,n=map(int,i.split());a-=(m<n)*n;b-=(n<m)*m
print(a,b)

###비교연산자

####숏코딩 3위
