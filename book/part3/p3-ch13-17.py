# # 답은 맞는데 시간초과...
# n,k = map(int,input().split())

# data = []
# temp = [[0] * n for _ in range(n)]
# dx = [-1,0,1,0]
# dy = [0,1,0,-1]

# for i in range(n):
#     data.append(list(map(int,input().split())))
# s,x,y = map(int,input().split())

# def virus(num):
#     for p in range(n):
#         for q in range(n):
#             if data[p][q] == num:
#                 for r in range(4):
#                     nx = p + dx[r]
#                     ny = q + dy[r]
#                     if nx >= 0 and nx < n and ny >= 0 and ny < n:
#                         if data[nx][ny] == 0:
#                             temp[nx][ny] = num
#     for a in range(n):
#         for b in range(n):
#             data[a][b] += temp[a][b]
#             temp[a][b] = 0
    
# time = 0

# while time < s:
#     for i in range(1,k+1):
#         virus(i)
#     time += 1

# print(data[x-1][y-1])

# 정답 풀이
from collections import deque

n,k = map(int,input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((graph[i][j],0,i,j))
            
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int,input().split())

dx = [-1,0,1,0]
dy = [0,1,0,-1]

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus,s+1,nx,ny))
                
print(graph[target_x -1][target_y -1])