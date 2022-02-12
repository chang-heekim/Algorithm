T = int(input())

times = [300, 60, 10]
answer = []
for time in times:
    if time > T:
        answer.append(0)
    elif time <= T:
        answer.append(T // time)
        T %= time

if T != 0:
    print(-1)
else:
    for a in answer:
        print(a, end=' ')
