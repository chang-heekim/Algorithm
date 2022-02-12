import re

def solution(new_id):
    #1
    new_id = new_id.lower()
    print(new_id)
    # 2
    new_id = re.sub('[^a-zA-Z0-9-_.]','', new_id)    
    print(new_id)
    # 3
    new_id = re.sub('[.{}]+', '.', new_id)
    print(new_id)
    #4
    if new_id.startswith('.'):
        new_id = new_id[1:]
    if len(new_id) > 0:
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    #5
    if new_id == '':
        new_id += 'a'
    print(new_id)
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    print(new_id)
    #7
    if len(new_id) <= 2:
        while len(new_id) != 3:
            new_id = new_id + new_id[-1]
    print(new_id)
    answer = new_id
    return answer