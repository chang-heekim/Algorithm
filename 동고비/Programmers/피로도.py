from itertools import permutations

def solution(k, dungeons):
    n = len(dungeons)
    answer = []
    for lst in permutations(dungeons, n):
        rest = k
        cnt = 0
        for i in range(len(lst)):
            if rest >= lst[i][0]:
                rest -= lst[i][1]
                cnt += 1
        answer.append(cnt)
    
    return max(answer)