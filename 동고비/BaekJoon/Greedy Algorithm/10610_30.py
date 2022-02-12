N = list(str(input()))

N.sort(reverse=True)
num = int(''.join(N))
if num % 30 == 0:
    print(num)
else:
    print(-1)