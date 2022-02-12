def solution(nums):
    count = int(len(nums) / 2)
    lst = len(list(set(nums)))
    print(list(set(nums)))
    if lst > count:
        answer = count
    else:
        answer = lst
    return answer