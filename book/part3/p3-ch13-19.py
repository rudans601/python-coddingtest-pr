# from collections import deque
# n = int(input())
# data = list(map(int,input().split()))
# num = 0
# for i in range(len(data)):
#     num += data[i]
# c = list(map(int,input().split()))

# max_num = 0
# min_num = 1e9

# q = deque()
# q.append(data[0])

# for i in range(1,n):
#     while q:
#         now = q.popleft()
#         for j in range(num):
#             pass
#     num -= 1
    
# 정답 풀이

n = int(input())
data = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
min_value = 1e9
max_value = -1e9

def divide(num1, num2):
    if num1 > 0:
        return num1 // num2
    else:
        num1 = -num1
        return -(num1//num2)
    
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i+1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i+1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i+1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, divide(now , data[i]))
            div += 1

dfs(1, data[0])

print(max_value)
print(min_value)

