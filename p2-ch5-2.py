# 내풀이 오답
from collections import deque

n,m = map(int,input().split())
graph = []

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x):
    v = q.popleft()
    print(v[0][1])

        
q = deque([0,0])
graph[0][0] = 1
bfs(q)

# 먼저 큐 만들고 첫 좌표 0,0 큐에 넣기

#bfs 함수 만들고 실행되면
#pop먼저 하고, 나온 값들을 graph에 count 표시하고, count는 1 증가
#나온 값들의 상하좌우에 방문을 안했으면 (graph에 1이라면) 전부 큐에 넣기
#이걸 반복해 n-1,m-1에 다가갈때 count출력

# 해답
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))
# 다시

n,m = map(int,input().split())
graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(n):
    graph.append(list(map(int,input())))

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]
        
print(bfs(0,0))