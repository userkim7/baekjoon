#1081

#L보다 크거나 같고, U보다 작거나 같은 모든 정수의 각 자리의 합을 구하는 프로그램을 작성하시오.

##첫째 줄에 두 정수 L과 U이 주어진다.
##첫째 줄에 문제의 정답을 출력한다.

def f(num): #1019:1~num까지 0~9의 개수 세기
    n=len(num)-1
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
    return sum([index*element for index,element in enumerate(count)]) #1~num까지 각 자리수 전체의 합
L,U=map(int,input().split())
if L:
    L=f(str(L-1)) #U-L 미만의 합
U=f(str(U)) #U이하의 합
print(U-L) #==차집합

###수열,거듭제곱,경우의 수
