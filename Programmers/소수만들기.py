from itertools import combinations

def solution(nums):
    answer = 0
    lst = list(combinations(nums, 3))
    s = [sum(l) for l in lst]
    for num in s:
        count = 0
        for i in range(1, num):
            if num % i == 0:
                count += 1
        if count == 1:
            answer += 1

    return answer