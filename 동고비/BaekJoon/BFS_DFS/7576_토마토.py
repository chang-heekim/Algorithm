from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

M, N = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
graph = [list(map(int, input().split())) for _ in range(N)]
q = deque()
answer = 0

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            q.append((i, j))

bfs()

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(graph[i]))
print(answer - 1)
        