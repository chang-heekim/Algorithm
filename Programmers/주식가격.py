def solution(prices):
    answer = []
    for j in range(len(prices) - 1):
        count = 0
        for i in range(j + 1, len(prices)):
            if prices[j] <= prices[i]:
                count += 1
            else:
                count += 1
                break
        answer.append(count)
    answer.append(0)
    return answer