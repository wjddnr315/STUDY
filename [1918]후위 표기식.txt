import sys
stack=[]
def w(x):
    if x=='+' or x=='-': return 1
    elif x=='/' or x=='*': return 2
    else: return 0
for a in sys.stdin.readline().strip():
    if 'A'<=a<='Z': print(a,end='')
    elif a == '(': stack.append(a)
    elif a== ')':
        while stack:
            t= stack.pop()
            if t == '(':break
            print(t,end='') 
    else:
        while stack and w(a)<=w(stack[-1]) and stack[-1]!='(':  
            print(stack.pop(),end='')
        stack.append(a)
while stack:
    print(stack.pop(),end='')