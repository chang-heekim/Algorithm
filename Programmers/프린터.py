def solution(priorities, location):
    pos = [i for i in range(len(priorities))]
    arr = priorities.copy()
    i = 0
    while True:
        if arr[i] < max(arr[i+1:]):
            pos.append(pos.pop(i))
            arr.append(arr.pop(i))
        else:
            i += 1
        
        if arr == sorted(arr, reverse=True):
            break
            
    return pos.index(location) + 1