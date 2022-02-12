S = input()

lst = ['U', 'C', 'P', 'C']
flag = True

for l in lst:
    if l in S:
        flag = True
        idx = S.index(l)
        S = S[idx + 1:]
    else:
        flag = False
        break

if flag:
    print("I love UCPC")
else:
    print("I hate UCPC")
