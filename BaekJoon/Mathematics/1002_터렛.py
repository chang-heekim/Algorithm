import math 

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if r1 + r2 < distance:
        answer = 0
    elif r1 + r2 > distance:
        answer = 2
    else:
        answer = 1
    
    if x1 == x2 and y1 == y2 and r1 != r2:
        answer = 0
    elif x1 == x2 and y1 == y2 and r1 == r2:
        answer = 1
    elif x1 != x2 or y1 != y2:
        if r1 + r2 < distance:
            answer = 0
        elif r1 + r2 > distance:
            answer = 2
        else:
            answer = 1
    print(answer)
