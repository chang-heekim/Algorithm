N = int(input())

arr = [1, 1]
for i in range(2, N):
    num = arr[i - 2] + arr[i - 1]
    arr.append(num)

print(arr[N-1])