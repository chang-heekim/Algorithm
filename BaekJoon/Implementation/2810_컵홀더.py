n = int(input())

batch = str(input())

if 'LL' in batch:
    batch = batch.replace('LL', 'L')
    
cup = len(batch) + 1

people = batch.count('S') + 2 * batch.count('L')

print(min(cup, people))
   