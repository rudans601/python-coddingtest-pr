# https://school.programmers.co.kr/learn/courses/30/lessons/42626
# from queue import PriorityQueue

# que = PriorityQueue()

# def solution(scoville, K):
#     for i in scoville:
#         que.put(i)
    
#     answer = 0
    
#     while 1:
#         one = que.get()
#         two = que.get()
        
#         cul = one + (two * 2)
#         que.put(cul)
#         answer += 1
        
#         if que.get() < K and que.empty():
#             return -1
#         if que.get() >= K:
#             return answer
#         else:
#             continue
        
# print(solution([1,1,1,1,1],7))

# 정답풀이 논리는 맞는데 순서가 다름

import heapq
def solution(scoville, K):
    heapq.heapify(scoville) 
    answer = 0

    while scoville:
        least_spicy = heapq.heappop(scoville)  

        if least_spicy >= K:
            return answer
        
        if not scoville:
            return -1

        second_least_spicy = heapq.heappop(scoville)  
        new_food = least_spicy + (second_least_spicy * 2) 

        heapq.heappush(scoville, new_food)  
        answer += 1  

    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))  