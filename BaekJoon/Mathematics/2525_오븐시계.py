h, m = list(map(int, input().split()))
n_time = int(input())

h += n_time // 60
m += n_time % 60

if m >= 60:
    h += 1
    m -= 60
if h >= 24:
    h -= 24

print(h, m)