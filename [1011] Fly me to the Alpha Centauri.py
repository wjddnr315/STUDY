for _ in range(int(input())):
    x,y=map(int,input().split())
    c,d,p=2,2,2
    while d < y-x:
        d+=c
        if p % 2:
            c +=1 
        p+=1
        print(d,p,c)
    if 1 <= y-x <=2:
        print(y-x)
    else: print(p)
