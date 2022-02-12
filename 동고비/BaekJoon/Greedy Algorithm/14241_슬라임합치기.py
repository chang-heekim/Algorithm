N = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)

score = 0
total = 0

for i in range(N-1):
    score = arr[i] * arr[i+1]
    arr[i+1] = arr[i] + arr[i + 1]
    print(arr)
    print(score)
    total += score 

print(total)