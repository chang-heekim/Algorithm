def solution(arr):
    answer = []
    num_count = 0
    for num in arr:
        if num not in answer:
            answer.append(num)
        elif num == last_num:
            continue
        elif num in answer and last_num != num:
            answer.append(num)
        
        last_num = num
    return answer