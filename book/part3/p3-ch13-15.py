from collections import deque
# answer = [] # 추가

# def bfs(graph, start, visited):
#     queue = deque([start,0])
#     visited[start] = True
    
#     while queue:
#         temp = queue.popleft()
#         v = temp[0]
#         dis = temp[1]
#         print(temp,end=" ")
        
#         for i in graph[v]:
      
#             if not visited[i]:
#                 queue.append(i,dis + 1)
#                 visited[i] = True

# n,m,k,x = map(int,input().split())

# visited = [False] * (n+1)
# graph = [[] for _ in range(n+1)]

# for i in range(m):
#     a,b = map(int,input().split())
#     graph[a].append(b)
    
# bfs(graph,x,visited)
# answer.sort()
# if len(answer) != 0:
#     for i in answer:
#         print(i)
# else:
#     print(-1)

# 정답 풀이
n,m,k,x = map(int,input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)

distance = [-1] * (n+1)
distance[x] = 0

q = deque([x])
while q:
    now = q.popleft()
    for next_node in graph[now]:
        if distance[next_node] == -1:
            distance[next_node] = distance[now] + 1
            q.append(next_node)
            
check = False
for i in range(1,n+1):
    if distance[i] == k:
        print(i)
        check = True
if not check:
    print(-1)