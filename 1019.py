#1019

#지민이는 전체 페이지의 수가 N인 책이 하나 있다. 첫 페이지는 1 페이지이고, 마지막 페이지는 N 페이지이다. 각 숫자가 전체 페이지 번호에서 모두 몇 번 나오는지 구해보자.

##첫째 줄에 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
##첫째 줄에 0이 총 몇 번 나오는지, 1이 총 몇 번 나오는지, ..., 9가 총 몇 번 나오는지를 공백으로 구분해 출력한다.

num=input()
n=len(num)-1 #==math.log(int(num),10),자릿수-1
count=[0]*10
for index,i in enumerate(range(n,0,-1)):
    x=i*(10**(i-1))
    k=int(num[index])
    for j in range(1,10):
        count[j]+=x*k
    for j in range(1,k):
        count[j]+=10**i
    if k!=0:
        count[k]+=int(num[index+1:])+1
for i in range(1,int(num[-1])+1):
    count[i]+=1
if len(num)==1:
    m=int(num[-1])
else:
    m=((int(num[0])-1)*10**n+(int(num[1:])+1))*(n+1)
    for i in range(n):
        m+=9*10**i*(i+1)
count[0]+=m-sum(count[1:])
print(' '.join(map(str,count)))

###수열,거듭제곱
