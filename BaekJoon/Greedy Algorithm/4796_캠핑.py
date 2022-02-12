i = 1
while True:
    cnt = 0
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and  V == 0:
        break
    else:
        cycle = V // P
        cnt = L * cycle
        cnt += min(L, V - cycle * P)
    print(f"Case {i}: {cnt}")
    i += 1