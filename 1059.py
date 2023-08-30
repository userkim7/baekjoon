#1059

#정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.
#A와 B는 양의 정수이고, A < B를 만족한다.
#A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
#집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.

##첫째 줄에 집합 S의 크기 L이 주어진다. 둘째 줄에는 집합에 포함된 정수가 주어진다. 셋째 줄에는 n이 주어진다.
##첫째 줄에 n을 포함하는 좋은 구간의 개수를 출력한다.

L=input()
S=sorted(map(int,input().split()))
N=int(input())
if N in S:
    print(0)
else:
    M,m=0,0
    for num in S:
        if num<N:
            m=num
        elif num>=N:
            M=num
            break
    m+=1
    M-=1
    print((N-m)*(M-N+1)+(M-N)) #(N보다 작은 시작을 가지는 구간의 개수)+N을 시작으로 가지는 구간의 개수

###구간
