count = 1
sum = 0
num = int(input())

for i in range(num):
    sum = 0
    count = 1
    x = input()
    for i in range(len(x)): 
        if x[i] == 'O':
            sum += count
            count += 1
        elif x[i] == 'X':
            count = 1
    print(sum)