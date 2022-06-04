from itertools import permutations
N = int(input())

lst = list(range(1, N + 1))
for numbers in permutations(lst):
    for num in numbers:
        print(num, end=' ')
    print()