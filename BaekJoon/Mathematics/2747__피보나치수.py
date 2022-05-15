N = int(input())

arr = [1, 1]
if N <= 2:
    answer = arr[N - 1]
else:
    for i in range(2, N + 1):
        num = arr[i - 1] + arr[i - 2]
        arr.append(num)

    answer = arr[N - 1]
print(answer)