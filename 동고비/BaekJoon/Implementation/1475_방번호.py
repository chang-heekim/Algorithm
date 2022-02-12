N = input()
answer = [0] * 10

for i in range(len(N)):
    num = int(N[i])
    if num == 6 or num == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1

    else:
        answer[num] += 1

print(max(answer))