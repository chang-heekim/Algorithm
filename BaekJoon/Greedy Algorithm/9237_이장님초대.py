N = int(input())

days = list(map(int, input().split()))
days.sort(reverse=True)
total = []
for i, day in enumerate(days):
    total.append(day + (i + 1))

print(max(total) + 1)