N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for i in range(M):
    x = sum(arr[:2])
    arr[0] = x
    arr[1] = x
    arr.sort()

print(sum(arr))    

