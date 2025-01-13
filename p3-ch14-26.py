# n = int(input())

# que = []
# for _ in range(n):
#     que.append(int(input()))

# que.sort(reverse=True)

# sub_result = que[len(que)-1] + que[len(que)-2]
# result = sub_result
# que.pop()
# que.pop()
# while que:
#     sub_result += que.pop()
#     result += sub_result

# print(result)

#정답 풀이
import heapq

n = int(input())

heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap,data)

result = 0

while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap,sum_value)
    
print(result)