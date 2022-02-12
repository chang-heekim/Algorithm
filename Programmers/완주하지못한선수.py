def solution(participant, completion):
    for p in completion:
        idx = participant.index(p)
        participant.pop(idx)
    return participant[0]