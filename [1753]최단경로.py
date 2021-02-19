from queue import PriorityQueue
import sys

input = sys.stdin.readline
INF = sys.maxsize

V, E = map(int, input().split())
K = int(input())
K -= 1
adj = [[] for _ in range(V)]
vstd = [False] * V
dist = [INF] * V
prev = [-1] * V
for i in range(E):
    u, v, w = map(int, input().split())
    adj[u - 1].append((v - 1, w))
dist[K] = 0
pq = PriorityQueue()
pq.put((0, K))
while not pq.empty():
    _, curr = pq.get()
    if vstd[curr]:
        continue
    vstd[curr] = True
    for nxt, nxt_cost in adj[curr]:
        if dist[curr] + nxt_cost < dist[nxt]:
            dist[nxt] = dist[curr] + nxt_cost
            pq.put((dist[nxt], nxt))

for i in dist:
    print(i if i != INF else "INF")
