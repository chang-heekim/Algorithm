arr = list(map(int, input().split()))
if arr[2] <= arr[1]:
    x = -1
else:
    x = int(arr[0] / (arr[2] - arr[1]) + 1)

print(x)