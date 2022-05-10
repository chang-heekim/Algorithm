num = list(map(int, input().split()))
lst = [n ** 2 for n in num]
answer = sum(lst) % 10
print(answer)