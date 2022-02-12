import sys 
from collections import Counter
input = sys.stdin.readline

numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
numbers.sort()

num = Counter(numbers).most_common(2)

print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
if len(numbers) > 1:
    if num[0][1] == num[1][1]:
        print(num[1][0])
    else:
        print(num[0][0])
else:
    print(num[0][0])
print(max(numbers) - min(numbers))

