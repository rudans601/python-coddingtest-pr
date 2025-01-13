n, m = map(int,input().split())
l = list(map(int,input().split()))

count = 0

for i in range(n):
    for j in  range(i,n):
        if i != j and l[i] != l[j]:
            count += 1

print(count)

# 정답풀이
n, m = map(int,input().split())
data = list(map(int,input().split()))

array = [0] * 11
for x in data:
    array[x] += 1
    
result = 0
for i in range(1,m+1):
    n -= array[i]
    result += array[i] * n

print(result)