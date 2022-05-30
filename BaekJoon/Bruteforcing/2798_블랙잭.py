from itertools import combinations

n, m = map(int, input().split())
arr = list(map(int, input().split()))
lst = list(combinations(arr, 3))
answer = []
for l in lst:
    if sum(l) <= m:
        answer.append(sum(l))

print(max(answer))