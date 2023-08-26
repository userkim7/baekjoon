#1002
#조규현의 좌표 
#(x1,y1)와 백승환의 좌표 
#(x2,y2)가 주어지고, 조규현이 계산한 류재명과의 거리 
#r1과 백승환이 계산한 류재명과의 거리 
#r2가 주어졌을 때, 류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

##첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 다음과 같이 이루어져 있다.
##한 줄에 공백으로 구분 된 여섯 정수 x1,y1,r1,x2,y2,r2가 주어진다.
##각 테스트 케이스마다 류재명이 있을 수 있는 위치의 수를 출력한다. 만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1출력한다.

for i in range(int(input())): #T번 반복
    x1,y1,r1,x2,y2,r2=map(int,input().split()) #x1,y1,r1,x2,y2,r2 입력
    l=((x2-x1)**2+(y2-y1)**2)**(1/2) #두 좌표간의 거리
    if l==0 and r1==r2: #같은 원
        print(-1)
    elif abs(r1-r2)<l<r1+r2: #두 점에서 만남
        print(2)
    elif l==abs(r1-r2) or l==r1+r2: #외접원/내접원
        print(1)
    else: #만나지 않음
        print(0)

###원리: 원의 방정식
