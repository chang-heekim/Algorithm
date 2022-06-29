N = int(input())
nines = [int('9'+'0'*i) for i in range(0, len(str(N)))]
result = 0

for i, s in enumerate(nines):
    if s == nines[-1]:
        result += len(str(s)) * (N - sum(nines[:-1]))
    else :
        i += 1
        result += i*s
print(result)