burger = []
soda = []
for _ in range(3):
    burger.append(int(input()))

for _ in range(2):
    soda.append(int(input()))

min_burger = min(burger)
min_soda = min(soda)
answer = min_burger + min_soda
print(answer - 50)