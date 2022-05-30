def solution(x):
    x = str(x)
    total = [int(a) for a in x]
    total = sum(total)
    if int(x) % total == 0:
        answer = True
    else:
        answer = False
    return answer