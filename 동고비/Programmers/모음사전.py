from itertools import product

def solution(word):
    
    d = []
    for i in range(1,6) :
        d += list(map(''.join, product("AEIOU", repeat = i)))
    d.sort()

    answer = d.index(word) + 1
    
    return answer