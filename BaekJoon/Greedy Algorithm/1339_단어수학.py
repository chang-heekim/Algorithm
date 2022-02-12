N = int(input())

words = []
for _ in range(N):
    words.append(input())

dic = {}

for word in words:
    x = len(word) - 1
    for w in word:
        if w in dic:
            dic[w] += pow(10, x)
        else:
            dic[w] = pow(10, x)
        x -= 1

lst = [d for d in dic.values()]
lst.sort(reverse=True)

result = 0
m = 9
for l in lst:
    result += l * m
    m -= 1

print(result)
