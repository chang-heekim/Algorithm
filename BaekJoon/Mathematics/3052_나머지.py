arr = []
for i in range(10):
    x = int(input())
    x = x % 42
    arr.append(x)

print(len(set(arr)))