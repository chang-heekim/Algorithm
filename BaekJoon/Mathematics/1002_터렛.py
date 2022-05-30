import math 

N = int(input())
for _ in range(N):
    x1, y1, r1, x2, y2, r2 = list(map(int, input().split()))
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if distance == 0 and r1 == r2:
        answer = -1
    elif abs(r1-r2) == distance or r1 + r2 == distance:  
        answer = 1
    elif abs(r1-r2) < distance < (r1+r2):
        answer = 2
    else:
        answer = 0
    
    print(answer)
    

