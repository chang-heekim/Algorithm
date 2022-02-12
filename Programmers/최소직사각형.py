def solution(a):
    for i in range(len(a)):
        if a[i][0] < a[i][1]:
            b = a[i][0]
            a[i][0] = a[i][1]
            a[i][1] = b
            
    return sorted(a)[len(a)-1][0] * sorted(a, key=lambda x: x[1])[len(a) - 1][1]