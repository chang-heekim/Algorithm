while True:
    try:
        S, T = input().split()

        j = 0
        f = False
        for i in range(len(T)):
            if T[i] == S[j]:
                j += 1
                if j == len(S):
                    f = True
                    break
        if f:
            print('Yes')
        else:
            print("No")
    except:
        break