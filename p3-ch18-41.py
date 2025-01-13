def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())
parent = [0] * (n + 1)
for i in range(1,n+1):
    parent[i] = i
graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent,i+1,j+1)

plan = list(map(int,input().split()))
p = parent[plan[0]]

result = True
for i in range(1,len(plan)):
    if parent[plan[i]] != p:
        result = False
        print("NO")
        break

if result:
    print("YES")
    
#정답맞춤

# 정답코드는 plan에서 find_parent를 이용해서 부모 루트 확인함