equation = input()

equation = equation.split('-')
answer = []
for e in equation:
    e = e.split('+')
    s = 0 
    for x in e:
        s += int(x)
    answer.append(s)

print(answer[0] - sum(answer[1:]))



