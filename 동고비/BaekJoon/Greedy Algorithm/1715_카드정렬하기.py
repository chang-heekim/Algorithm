import heapq

N = int(input())

cards = []
for _ in range(N):
    cards.append(int(input()))

heapq.heapify(cards)
count = 0

while len(cards) != 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    count += a + b

print(count)