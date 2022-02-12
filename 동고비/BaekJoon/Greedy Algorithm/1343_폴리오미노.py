S = input()
S = S.split('.')
B = True

for i in range(len(S)):
    a = 0
    b = 0
    while True:
        cnt = S[i].count('X')
        if cnt >= 4:
            S[i] = S[i].replace('XXXX', 'AAAA')
        else:
            if cnt == 2:
                S[i] = S[i].replace('XX', 'BB') 
            else:
                if cnt != 0:
                    B = False

        if not B or S[i].count('X') == 0:
            break
        
if not B:
    print(-1)
else:
    print('.'.join(S)) 

