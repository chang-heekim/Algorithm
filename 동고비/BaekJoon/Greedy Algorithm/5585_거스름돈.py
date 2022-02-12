N = int(input())

changes = [500, 100, 50, 10, 5, 1]
change = 1000 - N
i = 0
cnt = 0
while change:
    if changes[i] > change:
        i += 1
    elif changes[i] <= change:
        cnt += change // changes[i]
        change %= changes[i]

print(cnt)