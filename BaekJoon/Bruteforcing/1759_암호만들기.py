from itertools import combinations

l, c = map(int, input().split())

arr = list(input().split())
arr.sort()

word = ['a', 'i', 'e', 'o', 'u']

lst = list(combinations(arr, l))

for seq in lst:
    cnt1 = 0
    cnt2 = 0
    for i in range(l):
        if seq[i] in word:
            cnt1 += 1
        else:
            cnt2 += 1
    if cnt1 >= 1 and cnt2 >= 2:
        print(''.join(seq))