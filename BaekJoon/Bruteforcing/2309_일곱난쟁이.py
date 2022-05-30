arr = []
for i in range(9):
    arr.append(int(input()))

arr.sort(reverse=True)
stop = False
s = sum(arr)
rest = s - 100
rest

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i] + arr[j] == rest:
            stop = True
            break
    if stop:
        break
arr.pop(j)
arr.pop(i)
arr = arr[::-1]
for i in range(len(arr)):
    print(arr[i])