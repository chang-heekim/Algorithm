def solution(dartResult):
    standard = {'S' : 1, 'D' : 2, 'T' : 3, '*' : 2, '#' : -1}
    last_score = ''
    score = 0
    answer = []
    for point in dartResult:
        if point in standard:
            if point == 'S' or point == 'D' or point == 'T':
                score = int(last_score) ** standard[point]
                answer.append(score)

            elif point == '*':
                answer[-1] = answer[-1] * 2
                if len(answer) >= 2:
                    answer[-2] = answer[-2] * 2

            else:
                answer[-1] = answer[-1] * -1
            last_score = ''
        else:
            last_score += point

    return sum(answer)