N = int(input())

rope = []
for _ in range(N):
    rope.append(int(input()))

rope.sort()
m = 0
for i in range(len(rope)):
    if m < N * rope[i]:
        m = N * rope[i]
        N -= 1
    else:
        N -= 1
print(m)
