N, K = map(int, input().split())
number = list(input())
stack, k = [], K

for i in range(N):
    while k > 0 and stack and stack[-1] < number[i]:
        stack.pop()
        k -= 1
    stack.append(number[i])

print(''.join(stack[:N-K]))
