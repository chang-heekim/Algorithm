N = int(input())
for _ in range(N):
    a, b = map(int, input().split())

    num = a * b
    while b:
        a, b = b, a % b

    print(num // a)