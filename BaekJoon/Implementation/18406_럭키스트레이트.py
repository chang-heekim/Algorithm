n = int(input())
depth = len(str(n)) // 2
s1 = list(map(int, str(n)[:depth]))
s2 = list(map(int, str(n)[depth:]))

if sum(s1) == sum(s2):
    print('LUCKY')
else:
    print('READY')