import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = 1
graph = [[] for i in range(n+1)]

distance = [INF] * (n + 1)

for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1)) #양방향 추가 안해줌
    
def dijkstra(start):
    q = []
    
    heapq.heappush(q,(0,start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)
# long_po = 0
# long_dist = 0
# for i in range(1, n+1):
#     if distance[i] > long_dist and distance[i] != INF:
#         long_dist = distance[i]
#         long_po = i

# long_num = distance.count(long_dist)

# print(long_po,long_dist,long_num)
# # 위치가 틀렸음

#정답 코드
max_node = 0
max_distance = 0
result = []

for i in range(1,n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]:
        result.append(i)

print(max_node,max_distance, len(result))