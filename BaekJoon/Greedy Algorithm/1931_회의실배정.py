N = int(input())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

room.sort(key=lambda x: x[0])
room.sort(key=lambda x: x[1])
last = 0
cnt = 0

for start, end in room:
    if start >= last:
        cnt += 1
        last = end
print(cnt)