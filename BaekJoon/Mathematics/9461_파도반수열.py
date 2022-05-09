arr = [1, 1, 1, 2, 2]

for i in range(4, 101):
    number = arr[i] + arr[i - 4]
    arr.append(number)

N = int(input())
for _ in range(N):
    M = int(input())
    print(arr[M - 1])
