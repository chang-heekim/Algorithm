import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())

    grade = []
    for _ in range(N):
        grade.append(list(map(int, input().split())))

    grade.sort()
    cnt = 0
    g = grade[0][1]
    for i in range(len(grade)):
        if g > grade[i][1]:
            g = grade[i][1]
            cnt += 1

    print(cnt + 1)