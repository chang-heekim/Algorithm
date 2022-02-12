N, K = map(int, input().split())
count = 0

prices = []
for _ in range(N):
    prices.append(int(input()))

prices.sort(reverse=True)
for price in prices:
    if K // price < 1:
        continue
    else:
        count += K // price
        K %= price

print(count)