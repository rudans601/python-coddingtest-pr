# n = int(input())
# t = []
# p = []
# for _ in range(n):
#     a,b = map(int,input().split())
#     t.append(a)
#     p.append(b)

# for i in range(n):
#     for j in range(i,n):
#         p[j + t[j]] = max(p[j + t[j]],p[j]+p[j + t[j]])

# print(max(p))

# 정답 풀이

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x,y = map(int,input().split()) 
    t.append(x)
    p.append(y)
    
for i in range(n-1,-1,-1):
    time = t[i] + i
    
    if time <= n:
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)