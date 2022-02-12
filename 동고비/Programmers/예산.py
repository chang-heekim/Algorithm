def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in range(len(d)):
        budget -= d[i]
        if budget < 0:
            break
        answer += 1
    return answer