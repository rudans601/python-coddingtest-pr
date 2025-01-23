# from collections import queue
# n,l,r = map(int,input().split())
# union = []
# for i in range(n):
#     union.append(list(map(int,input().split())))

# count = 0 #인구 이동 횟수
# q = queue()
# sum = 0 # 인구 합계
# while 1:
#     for i in range(n):
#         for j in range(n):
            
#             for dx,dy in [[-1,0],[0,1],[1,0],[0,-1]]:
#                 nx = i + dx
#                 ny = j + dy
#                 if l <= abs(union[nx][ny] - union[i][j]) <= r and (nx,ny) not in q:
#                     q.append((nx,ny))
#                     sum += union[nx][ny]
#                     if (i,j) not in q:
#                         q.append((i,j))
#                         sum += union[i][j]
#     while q:
#         a,b = q.popleft()
#         union[a][b] = sum // len(q)
        
#     count += 1

# print(count)

# 정답 풀이
from collections import deque

n,l,r = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,-1,0,1]

result = 0

def process(x,y,index):
    united = []
    united.append((x,y))
    
    q = deque()
    q.append((x,y))
    union[x][y] = index
    summary = graph[x][y]
    count = 1
    
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append((nx,ny))
                    union[nx][ny] = index
                    summary += graph[nx][ny]
                    count += 1
                    united.append((nx,ny))
                    
    for i,j in united:
        graph[i][j] = summary // count

total_count = 0    
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                process(i,j,index)
                index += 1
    if index == n * n:
        break
    total_count += 1

print(total_count)