def solution(food_times, k):
    answer = 0
    cur = 0
    n = 0
    while n < k:
        if food_times[cur] != 0:
            food_times[cur] -= 1
            n += 1
            cur += 1
            if cur >= len(food_times):
                cur %= len(food_times)
        elif food_times[cur] == 0:
            cur += 1

    return answer
# 정답 풀이
import heapq
def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q,(food_times[i], i + 1))
        
    sum_value = 0
    previous = 0
    
    length = len(food_times)
    
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous) * length
        length -= 1
        previous = now
        
    result = sorted(q,key=lambda x: x[1])
    return result[(k-sum_value) % length][1]