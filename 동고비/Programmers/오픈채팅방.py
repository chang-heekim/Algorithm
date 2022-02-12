def solution(record):
    lst = {}
    stack = []
    for r in record:
        r = r.split()
        if r[0] == 'Enter':
            lst[r[1]] = r[2]
            stack.append(r[1])
        elif r[0] == 'Leave':
            stack.append('-' + r[1])
        elif r[0] == 'Change':
            lst[r[1]] = r[2]

    answer = []
    for s in stack:
        if s.startswith('-'):
            answer.append(f'{lst[s[1:]]}님이 나갔습니다.')
        else:
            answer.append(f'{lst[s]}님이 들어왔습니다.')
    
    return answer