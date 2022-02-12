from collections import deque

T = int(input())
for _ in range(T):
    lst = []
    N = int(input())
    card_lst = deque(input().split())
    lst.append(card_lst.popleft())
    while card_lst:
        temp = card_lst.popleft()
        if temp > lst[0]:
            lst.append(temp)
        else:
            lst.insert(0,temp)

    print(''.join(lst))