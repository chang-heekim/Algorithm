N, L = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

for height in heights:
    if L >= height:
        L += 1
    else:
        break

print(L)