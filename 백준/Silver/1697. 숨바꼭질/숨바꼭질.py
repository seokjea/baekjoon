from collections import deque
n,k = map(int,input().split()) #n=위치, k = 동생 위치

visited = [False] * 100001

def bfs(start):
    queue = deque()
    queue.append((start,0)) # (위치, 시간간)
    visited[start] = True
    while queue:
        x, time = queue.popleft()
        if x == k:
            return time
        
        for next_pos in (x * 2, x-1 ,x+1):
            if 0 <= next_pos <= 100000 and not visited[next_pos]:
                queue.append((next_pos, time + 1))
                visited[next_pos] = True
print(bfs(n))
      
                                      
            