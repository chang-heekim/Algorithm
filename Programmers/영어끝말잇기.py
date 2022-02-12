def solution(n, words):
    stack = []
    people = 0
    seq = 0
    rest_word = words[0][0]
    for idx, word in enumerate(words):
        if len(word) == 1 or rest_word != word[0]:
            people = idx % n + 1 
            seq = idx // n + 1
            break
        if word not in stack:
            stack.append(word)
        elif word in stack:
            people = idx % n + 1 
            seq = idx // n + 1
            break
            
        rest_word = word[-1]

    return [people, seq]