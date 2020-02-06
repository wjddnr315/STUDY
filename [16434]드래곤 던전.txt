import sys
n,h_atk = map(int,input().split())
a=[]
for i in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
l= 1
r= 9223372036854775807
while l<=r:
    mid=(l+r)//2
    h_cur=mid
    atk=h_atk
    for i in range(n):
        if a[i][0]==1:
            c = a[i][2]//atk
            if a[i][2] % atk== 0 : h_cur-= (c-1)*a[i][1]
            else : h_cur-=c*a[i][1]
            if h_cur<=0: break
        elif a[i][0]==2:
            atk+=a[i][1]
            if mid>h_cur+a[i][2]: h_cur+=a[i][2]
            else :h_cur = mid
    if h_cur > 0 : r = mid-1
    else : l = mid+1
print(l)
