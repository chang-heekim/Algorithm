number = list(map(str, input().split()))

a = number[0][::-1]
b = number[1][::-1]

if a > b:
    print(a)
else:
    print(b)