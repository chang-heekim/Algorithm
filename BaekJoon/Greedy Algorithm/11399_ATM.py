N = int(input())
time = list(map(int, input().split()))

time.sort()
answer = 0
s = 0
for t in time:
    s += t
    answer += s

print(answer)