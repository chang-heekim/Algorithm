import sys 
input = sys.stdin.readline 
G = int(input())
P = int(input())
cnt = 0
parent = [i for i in range(G + 1)]

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    parent[b] = a

for _ in range(P):
    num = int(input())
    x = find(num)
    if x == 0:
        break
    cnt += 1
    union(x-1, x)

print(cnt)
