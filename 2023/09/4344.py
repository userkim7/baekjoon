#4344

for i in[*open(0)][1:]:
  a,*b=map(int,i.split())
  print(f'{sum(j*a>sum(b)for j in b)/a:.3%}')

###평균

####숏코딩 6위
for i in[*open(0)][1:]:a,*b=map(int,i.split());print(f'{sum(j*a>sum(b)for j in b)/a:.3%}')
