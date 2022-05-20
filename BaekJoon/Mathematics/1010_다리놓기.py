import math

N = int(input())
for _ in range(N):
    n, m = map(int, input().split(' '))
    arr = [0] * m
    print(math.comb(m, n))
