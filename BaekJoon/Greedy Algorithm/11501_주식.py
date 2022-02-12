T = int(input())
for i in range(T):
    N = int(input())
    prices = list(map(int, input().split()))
    
    answer = 0
    Max = prices[-1]
    
    for i in range(len(prices)-2, -1, -1):
        if prices[i] > Max:
            Max = prices[i]
        else:
            answer += Max-prices[i]
    print(answer)