def solution(arr):
    min_num = min(arr)
    index = arr.index(min_num)
    answer = [arr[i] for i in range(len(arr)) if i != index]
    if len(answer) == 0:
        answer = [-1]
    return answer