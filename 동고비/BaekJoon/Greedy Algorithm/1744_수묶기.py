N = int(input())

plus = []
minus = []
answer = []
for _ in range(N):
    x = int(input())
    if x > 0:
        plus.append(x)
    else:
        minus.append(x)

plus.sort()
minus.sort(reverse=True)
while plus:
    if len(plus) == 1:
        answer.append(plus.pop())
        break
    x = plus.pop()
    y = plus.pop()
    if x == 1 or y == 1:
        answer.append(x + y)
    else:
        answer.append(x * y) 

while minus:
    if len(minus) == 1:
        answer.append(minus.pop())
        break
    x = minus.pop()
    y = minus.pop()
    answer.append(x * y)

print(sum(answer))
