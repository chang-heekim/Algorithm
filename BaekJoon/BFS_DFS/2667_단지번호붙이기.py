from collections import deque

N = int(input())
graph = []

for _ in range(N):
    graph.append(list(map(int, input())))
    
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
answer = 0
count = []

def bfs(i, j):
    q = deque()
    q.append((i, j))
    graph[i][j] = 0
    cnt  = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue 
            if graph[nx][ny] == 1:
                q.append((nx, ny))
                graph[nx][ny] = 0
                cnt += 1 
    return cnt 

for i in range(N):
    for j in range(N):
        cnt = 0
        if graph[i][j] == 1:
            count.append(bfs(i, j))
            answer += 1

print(answer)
count.sort()
for c in count:
    print(c)