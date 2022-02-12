ans = []
for i in range(7):
    num = int(input())
    if num % 2 != 0:
        ans.append(num)
if len(ans) != 0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)