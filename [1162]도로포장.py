import sys
import heapq

INF = sys.maxsize
input = sys.stdin.readline
N, M, K = map(int, input().split())
K += 1
vstd = [[False] * K for _ in range(N)]
dist = [[INF] * K for _ in range(N)]

adj = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    adj[u - 1].append((v - 1, w))
    adj[v - 1].append((u - 1, w))
h = []
heapq.heappush(h, (0, 0, K - 1))

for i in range(K):
    dist[0][i] = 0

while h:
    _, curr, k = heapq.heappop(h)
    if vstd[curr][k]:
        continue
    vstd[curr][k] = True
    for nxt, d in adj[curr]:
        if dist[curr][k] + d < dist[nxt][k]:
            dist[nxt][k] = dist[curr][k] + d
            heapq.heappush(h, (dist[nxt][k], nxt, k))
            if k > 0:
                if dist[nxt][k - 1] > dist[curr][k]:
                    dist[nxt][k - 1] = dist[curr][k]
                heapq.heappush(h, (dist[nxt][k - 1], nxt, k - 1))
print(min(dist[-1]))
