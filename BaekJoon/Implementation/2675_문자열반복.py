count = int(input())

for _ in range(count):    
    num, s = input().split()
    num = int(num)
    answer = ''
    for i in range(len(s)):
        answer += s[i] * num
    print(answer)