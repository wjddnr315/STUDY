from itertools import combinations
n,k=map(int,input().split())
k-=5
if k <0:
    print(0);exit() 
l={'a','t','i','c','n'}
words,alpha=[],[chr(ord('a')+i) for i in range(26)]
alpha=set(alpha)-l
res=0
for _ in range(n):
    w=set(input())-l
    words.append(w)
for c in combinations(alpha,k):
    cnt=0
    c=set(c)
    for word in words:
        if word&c == word:
            cnt+=1
    res=max(res,cnt)
print(res)


