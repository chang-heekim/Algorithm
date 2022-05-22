x, y = map(int, input().split())

d = [True] * (y + 1)

for i in range(2, int(pow(y, 1/2)) + 1):
    if d[i] == True:
        j = 2
        while i * j <= y:
            d[i * j] = False
            j += 1

for i in range(x, y + 1):
    if i > 1 and d[i]:
        print(i)