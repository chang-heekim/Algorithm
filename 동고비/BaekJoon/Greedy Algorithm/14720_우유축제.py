N = int(input())
x = list(map(int, input().split()))

cnt = 0

for i in range(N):
    if x[i] == cnt % 3:
        cnt += 1

print(cnt)
