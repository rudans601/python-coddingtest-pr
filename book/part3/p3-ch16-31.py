# t = int(input())
# for _ in range(t):
#     n,m = map(int,input().split())
#     ground = [[0] * m for _ in range(n)]
#     sum = [[0] * m for _ in range(n)]
#     temp = list(map(int,input().split()))
#     k = 0
#     for i in range(n):
#         for j in range(m):
#             ground[i][j] = temp[k]
#             if j == 0:
#                 sum[i][j] = temp[k]
#             k += 1
#     for i in range(n):
#         for j in range(m):
#             if i - 1 < n and j + 1 < m:
#                 sum[i-1][j+1] = max(sum[i-1][j+1], ground[i][j] + ground[i-1][j+1])
#             if i < n and j + 1 < m:
#                 sum[i][j+1] = max(sum[i][j+1], ground[i][j] + ground[i][j+1])
#             if i + 1 < n and j + 1 < m:
#                 sum[i+1][j+1] = max(sum[i+1][j+1], ground[i][j] + ground[i+1][j+1])
    
#     print(max(map(max,sum)))
    
# 정답 풀이
for tc in range(int(input())):
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    
    for j in range(1,m):
        for i in range(n):
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up,left_down,left)
    result = 0
    for i in range(n):
        result = max(result,dp[i][m-1])
    
    print(result)