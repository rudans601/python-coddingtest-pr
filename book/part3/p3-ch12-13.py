# from itertools import combinations

# def check(p,q):
#     min_len = 100000
#     for x in house:
#         min_len = min(min_len,abs(p - x[0]) + abs(q - x[1]))
#     return min_len

# chicken = []
# house = []

# n,m = map(int,input().split())
# city = []
# for i in range(1,n+1):
#     city.append(list(map(int,input().split())))

# for i in range(n):
#     for j in range(n):
#         if city[i][j] == 2:
#             chicken.append([i,j])
#         elif city[i][j] == 1:
#             house.append([i,j])

# result = list(combinations(chicken,m))
# total = 100000
# for a in result:
#     temp = 0
#     for b in a:
#         temp += check(b[0],b[1])
#     total = min(total,temp)

# print(total)

# 정답 풀이
from itertools import combinations
n,m = map(int,input().split())
chicken, house = [],[]

for r in range(n):
    data = list(map(int,input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))
candidates = list(combinations(chicken,m))

def get_sum(candidate):
    result = 0
    for hx,hy in house:
        temp = 1e9
        for cx,cy in candidate:
            temp = min(temp,abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
    
print(result)