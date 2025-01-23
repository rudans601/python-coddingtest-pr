# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# from collections import deque

# def solution(prices):
#     time = 0
#     move = [0] * len(prices)
    
#     while time < len(prices):
#         time += 1
#         for i in range(len(prices)):   
#             if prices[i] <= prices[time]:
#                 move[i] += 1
        
#     return move

# print(solution([1, 2, 3, 2, 3]))
# 정답 코드
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for i, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:
            top = stack.pop()
            answer[top] = i - top 
        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = len(prices) - 1 - top

    return answer

print(solution([1, 2, 3, 2, 3]))  # 출력: [4, 3, 1, 1, 0]