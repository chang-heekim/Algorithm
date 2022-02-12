import sys 
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    J, N = map(int, input().split())
    store = []
    for _ in range(N):
        R, C = map(int, input().split())
        store.append(R * C)
    store.sort(reverse=True)
    cnt = 0

    for i in range(len(store)):
        if store[i] >= J:
            cnt += 1
            break
        elif store[i] <= J:
            J = J - store[i]
            cnt += 1
        if J == 0:
            break

    print(cnt)
            