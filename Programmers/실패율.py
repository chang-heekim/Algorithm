def solution(N, stages):
    fail = {}
    length = len(stages)
    for i in range(1, N+1):
        if length != 0:
            count = stages.count(i)
            fail[i] = count / length
            length -= count
        else:
            fail[i] = 0
    return sorted(fail, key=lambda x: fail[x], reverse=True)