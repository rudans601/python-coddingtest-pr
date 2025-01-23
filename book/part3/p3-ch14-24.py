n = int(input())
data = list(map(int,input().split()))

data.sort()
min_sum = 1e9
a = -1
for i in data:
    sum = 0
    for j in data:
        sum += abs(i - j)
    if min_sum > sum:
        min_sum = sum
        a = i

print(a)

# 정답풀이

n = int(input())
data = list(map(int,input().split()))

data.sort()

print(data[(n-1) // 2])