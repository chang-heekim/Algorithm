import sys 
input = sys.stdin.readline
M = int(input())

S = []
for _ in range(M):
    cmd = input().split()

    if cmd[0] == 'add':
        if int(cmd[1]) in S:
            continue
        else:
            S.append(int(cmd[1]))

    elif cmd[0] == 'remove':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            continue
    
    elif cmd[0] == 'check':
        if int(cmd[1]) in S:
            print(1)
        else:
            print(0)
    
    elif cmd[0] == 'toggle':
        if int(cmd[1]) in S:
            S.remove(int(cmd[1]))
        else:
            S.append(int(cmd[1]))
    
    elif cmd[0] == 'all':
        S = list(range(1, 21))
    elif cmd[0] == 'empty':
        S = []