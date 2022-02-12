N, L = map(int, input().split())
loc = list(map(int, input().split()))

loc.sort()
prev = loc[0]
cnt = 1

for i in range(1, len(loc)):
    l = prev + L - 1

    if loc[i] <= l:
        continue
    else:
        prev = loc[i]
        cnt += 1

print(cnt)
