day = int(input())

num = list(map(int, input().split()))
answer = 0
for n in num:
    if str(day) == str(n)[-1]:
        answer += 1

print(answer)