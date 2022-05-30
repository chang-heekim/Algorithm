num = int(input())
sen = ''
for i in range(num):
    sentence = input().split()
    for j in range(len(sentence)):
        print(sentence[j][::-1], end=' ')