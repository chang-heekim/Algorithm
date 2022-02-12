from collections import deque

def solution(n, computers):
    
    def BFS(i):
        q = deque()
        q.append(i)
        
        while q:
            x = q.popleft()
            visited[x] = 1
            for a in range(n):
                if computers[x][a] and not visited[a]:
                    q.append(a)
                    
    answer = 0
    visited = [0 for i in range(len(computers))]
    for i in range(n):
        if not visited[i]:
            BFS(i)
            answer += 1
            
    return answer