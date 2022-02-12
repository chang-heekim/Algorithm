from collections import deque

N, M, V = map(int, input().split())
tree = [[] for _ in range(N + 1)]
v_dfs = [False] * (N + 1)
v_bfs = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
tree = [sorted(t) for t in tree]

def dfs(x):
    v_dfs[x] = True
    print(x, end=' ')
    for t in tree[x]:
        if not v_dfs[t]:
            dfs(t)

def bfs(x):
    q = deque()
    q.append(x)
    v_bfs[x] = True

    while q:
        p = q.popleft()
        print(p, end=' ')
        for t in tree[p]:
            if not v_bfs[t]:
                q.append(t)
                v_bfs[t] = True



dfs(V)
print()
bfs(V)


