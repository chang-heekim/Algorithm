num = int(input())
arr = list(map(int, input().split()))

sum = 0
for i in range(num):
    x = arr[i] / max(arr) * 100
    sum += x
print(sum / num)