from collections import deque

def solution(maps):

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    r = len(maps)
    c = len(maps[0])

    q = deque()
    q.append((0, 0))

    while q:
        y, x = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= ny < r and 0 <= nx < c and maps[ny][nx] == 1:
                if maps[ny][nx] == 1:
                    maps[ny][nx] = maps[y][x] + 1
                    q.append((ny, nx))

    if maps[-1][-1] == 1:
        return -1
    else:
        return maps[-1][-1]