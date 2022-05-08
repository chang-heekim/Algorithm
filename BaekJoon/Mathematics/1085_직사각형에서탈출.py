x, y, w, h = list(map(int, input().split()))

west = x
east = w - x
south = y
north = h - y

answer = [west, east, south, north]
print(min(answer))