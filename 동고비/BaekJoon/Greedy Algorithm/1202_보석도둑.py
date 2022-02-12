import heapq
import sys
input = sys.stdin.readline
N, K = map(int, input().split())

information = []
weights = []
answer = 0

for _ in range(N):
    M, V = map(int, input().split())
    heapq.heappush(information, [M, V])
for _ in range(K):
    weights.append(int(input()))

weights.sort()
price = []

for weight in weights:
    while information and weight >= information[0][0]:
        w, p = heapq.heappop(information)
        heapq.heappush(price, -p)

    if price:
        answer -= heapq.heappop(price)

print(answer)



