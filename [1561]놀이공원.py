n,m=map(int,input().split())
a=list(map(int,input().split()))
last=0
l=0
r=2000000000
cnt = 0
c=0
while l<=r:
    mid=(l+r)//2
    cnt=0
    for i in range(m):
        cnt+=(mid//a[i])+1
        if not mid%a[i]:last = i+1
    if cnt>=n:
        r= mid-1
    else:
        l=mid+1
        c=cnt
for i in range(m):
    if cnt == n: break
    if not l % a[i] :
        c +=1
        if c == n :
            last=i+1
print(last)
