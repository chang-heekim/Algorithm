def solution(phone_number):
    sec = '*' * len(phone_number[::-1][4:])
    answer = sec + phone_number[len(phone_number[4:]):]
    return answer