def solution(progresses, speeds):
    answer = []
    for idx, p in enumerate(progresses):
        rest = 100 - p
        if rest % speeds[idx] == 0:
            answer.append(rest // speeds[idx])
        else:
            answer.append(rest // speeds[idx] + 1)
    print(answer)
    first = answer.pop(0)
    lst = []
    count = 1
    
    for day in answer:
        if first == day:
            count += 1
        elif first > day:
            count += 1
        else:
            lst.append(count)
            first = day
            count = 1
    lst.append(count)
    
    return lst