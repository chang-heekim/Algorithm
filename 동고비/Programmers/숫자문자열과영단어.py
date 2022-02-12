import re 
def solution(s):
    answer = ''
    stop = False
    word = {
        0 : 'zero',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine'
    }
    words = ''
    for i in s:
        if i.isdigit():
            answer += i
            continue
        words += i
        for idx, w in enumerate(word):
            if words == word[idx]:
                answer += str(idx)
                words = ''
    return int(answer)