def solution(array, commands):
    answer = []
    for i, j, k in commands:
        arr = sorted(array[i-1:j])
        print(arr)
        answer.append(arr[k-1])
    return answer