for i in range(int(input())):
    x1,y1,r1,x2,y2,r2=map(int,input().split())
    l=((x2-x1)**2+(y2-y1)**2)**(1/2)
    if l==0 and r1==r2:
        print(-1)
    elif abs(r1-r2)<l<r1+r2:
        print(2)
    elif l==abs(r1-r2) or l==r1+r2:
        print(1)
    else:
        print(0)
