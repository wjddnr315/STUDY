import sys

input = sys.stdin.readline
n = int(input())
tree = dict()
parents = [0] * (n)


def dfs(vtx):
    vstd = [False] * n
    stack = [vtx]

    while stack:
        for _ in stack:
            _from = stack.pop()
            vstd[_from] = True
            for _to in tree[_from]:
                if parents[_to] == 0 and not vstd[_to]:
                    parents[_to] = _from
                    stack.append(_to)


for _ in range(n - 1):
    vtx1, vtx2 = map(int, input().split())
    vtx1 -= 1
    vtx2 -= 1
    if vtx1 not in tree:
        tree[vtx1] = [vtx2]
    else:
        tree[vtx1].append(vtx2)
    if vtx2 not in tree:
        tree[vtx2] = [vtx1]
    else:
        tree[vtx2].append(vtx1)
dfs(0)

for i in range(1, n):
    print(parents[i] + 1)
