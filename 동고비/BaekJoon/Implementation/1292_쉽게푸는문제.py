A, B = map(int, input().split())

lst = []
i = 1
while True:
    lst += [i] * i
    if len(lst) >= B:
        break
    i += 1

print(sum(lst[A-1:B]))
