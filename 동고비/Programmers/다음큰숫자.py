def solution(n):
    count_1 = bin(n).count('1')
    while True:
        n = n + 1
        count_2 = bin(n).count('1')
        
        if count_1 == count_2:
            break
    answer = n
    return answer