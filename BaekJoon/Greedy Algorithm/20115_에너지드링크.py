N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)

Sum = lst[0]
for i in range(1, len(lst)):
    Sum += lst[i] / 2

print(Sum)