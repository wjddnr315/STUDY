n,k,d=map(int,input().split())
a=[]
for i in range(k):
    a.append(list(map(int,input().split())))
l=1
r=1000000
while l<=r :
    mid=(l+r)//2
    s=0
    for i,j,t in a:
        if mid > j:
            if j-i>=0: s+=(j-i)//t+1
        else:
            q=mid-i if mid>i else 0
            if mid-i>=0: s+=q//t+1
    if s>=d :
        r=mid-1
    else:
        l=mid+1
print(l)
