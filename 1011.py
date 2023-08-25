#1011
#

##

for i in range(int(input())):
    x,y=map(int,input().split())
    if y-x==1 or y-x==2:
        print(y-x)
    else:
        d=y-x-2
        t=1
        n=2
        num=0
        while num<d:
            if t%2==0:
                num+=n
                n+=1
            else:
                num+=n
            t+=1
        print(t+1)
