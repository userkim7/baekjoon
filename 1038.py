#1038

#음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

##첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.
##첫째 줄에 N번째 감소하는 수를 출력한다.

from itertools import combinations
List=[]
for R in range(1,11):List+=list(combinations('9876543210',R))[::-1] #감소하는 수 리스트
try:
    print(''.join(List[int(input())])) #N번째 조합
except:
    print(-1) #없을 경우

###조합

####숏코딩 python3 6위
from itertools import*
l=[]
for R in range(1,11):l+=list(combinations('9876543210',R))[::-1]
try:print(''.join(l[int(input())]))
except:print(-1)
