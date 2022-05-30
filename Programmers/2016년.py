def solution(a, b):
    day = 'FRI SAT SUN MON TUE WED THU'.split()
    days =[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    x = 0
    for i in range(a - 1):
        x += days[i]
    
    x += b - 1
    x %= 7
    return day[x]