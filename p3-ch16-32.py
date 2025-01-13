# array = []
# dp = []
# for _ in range(int(input())):
#     temp = list(map(int,input().split()))
#     array.append(temp)
#     dp.append(temp)

# for i in range(len(array)):
#     for j in range(len(array[i])):
#         if i == 0:
#             left_up = 0
#         else:
#             left_up = array[i-1][j-1]
#         if i == len(array[i]) - 1:
#             right_up = 0
#         else:
#             right_up = array[i-1][j]
#         dp[i][j] = dp[i][j] + max(left_up,right_up)

# result = 0
# for i in range(len(array)):
#     result = max(result,dp[i][len(array[i])-1])
# print(result)

# 정답 풀이
n = int(input())
dp = []

for _ in range(n):
    dp.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        dp[i][j] = dp[i][j] + max(up,up_left)
        
print(max(dp[n-1]))