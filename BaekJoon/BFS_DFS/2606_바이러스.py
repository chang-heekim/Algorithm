from collections import deque
import collections

N = int(input())
M = int(input())
connections = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

def bfs(i):
    global cnt
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        x = q.popleft()
        for c in connections[x]:
            if not visited[c]:
                visited[c] = True
                q.append(c)
                cnt += 1
    return cnt

for _ in range(M):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

print(bfs(1))