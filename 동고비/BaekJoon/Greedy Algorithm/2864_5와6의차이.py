A, B = input().split()

min_A = A.replace('6', '5')
min_B = B.replace('6', '5')

Min = int(min_A) + int(min_B)

max_A = A.replace('5', '6')
max_B = B.replace('5', '6')

Max = int(max_A) + int(max_B)
print(Min, Max)