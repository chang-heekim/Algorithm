import sys
input = sys.stdin.readline

answer = []
for _ in range(int(input())): 
    K = int(input())
    if K != 0:
        answer.append(K)
    else:
        answer.pop()

print(sum(answer))
