N = int(input())
info = []
answer = []
for _ in range(N):
    w, h = map(int, input().split())
    info.append([w, h])


for i in range(N):
    count = 0
    for j in range(N):
        if info[i][0] < info[j][0] and info[i][1] < info[j][1]:
            count += 1
    answer.append(count + 1)

for ans in answer:
    print(ans, end=' ')