A, B = map(int, input().split())
N = int(input())
fre = []
x = 10001
for _ in range(N):
    fre.append(int(input()))

for f in fre:
    x = min(x, abs(f - B))

print(min(x + 1, abs(A - B)))