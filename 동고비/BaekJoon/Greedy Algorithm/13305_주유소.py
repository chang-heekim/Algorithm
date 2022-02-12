N = int(input())

distances = list(map(int, input().split()))
prices = list(map(int, input().split()))

min_price = prices[0]
s = 0
for i in range(N - 1):
    if min_price > prices[i]:
        min_price = prices[i]
    s += (min_price * distances[i])

print(s)