S = int(input())

N = 1
while True:
    if N * (N + 1) / 2 > S:
        break
    else:
        N += 1
print(N - 1)

