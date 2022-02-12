S = input()
lst = [0] * 26

for s in S:
    lst[ord(s) - 97] = S.count(s)

for l in lst:
    print(l, end=' ')