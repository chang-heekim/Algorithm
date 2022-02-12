lst = [25, 10, 5, 1]
N = int(input())
for i in range(N):
    money = int(input())
    for l in lst:
        if money >= l:
            print(money // l, end=' ')
            money %= l
        else:
            print(0, end=' ')
    print()