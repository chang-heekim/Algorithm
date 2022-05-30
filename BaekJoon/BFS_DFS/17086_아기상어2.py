import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]


dx = [0, 0, 1, -1, -1, -1, 1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]


def bfs(x, y):
    visit = [[0]*M for _ in range(N)]
    q = deque()

    visit[x][y] = 1
    q.append([x, y, 0])

    while q:
        x, y, cost = q.popleft()
        if board[x][y]:
            return cost

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if not visit[nx][ny]:
                    visit[nx][ny] = 1
                    q.append([nx, ny, cost + 1])


def solution():
    answer = 0

    for x in range(N):
        for y in range(M):
            if not board[x][y]:
                answer = max(answer, bfs(x, y))

    return answer


print(solution())