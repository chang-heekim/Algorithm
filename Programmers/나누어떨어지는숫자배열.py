def solution(arr, divisor):
    arr = sorted(arr)
    answer = []
    for num in arr:
        if num % divisor == 0:
            answer.append(num)
    if len(answer) == 0:
        answer = [-1]
    return answer