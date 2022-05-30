a, b = input().split()
answer = []
for m in range(len(b) - len(a) + 1):
    cnt = 0
    y = b[m: m + len(a)]
    for i in range(len(a)):
        if a[i] != y[i]:
            cnt += 1
    answer.append(cnt)
print(min(answer))