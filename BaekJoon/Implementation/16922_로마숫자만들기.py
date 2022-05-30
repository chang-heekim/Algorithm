from itertools import combinations_with_replacement
num_lst = ['I', 'V', 'X', 'L']
n = int(input())
lst = list(combinations_with_replacement(num_lst, n))

answer = []
for layer in lst:
    s = 0
    for i in range(len(layer)):
        if layer[i] == num_lst[0]:
            s += 1
        elif layer[i] == num_lst[1]:
            s += 5
        elif layer[i] == num_lst[2]:
            s += 10
        elif layer[i] == num_lst[3]:
            s += 50
    answer.append(s)

print(len(set(answer)))