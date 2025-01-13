# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
def solution(priorities, location):
    que = deque()
    pri = deque(priorities)
    for i in range(len(priorities)):
        que.append(i)
    answer = 0
    while que:
        now = que.popleft()
        now_pri = pri.popleft()
        if pri and max(pri) > now_pri:
            que.append(now)
            pri.append(now_pri)
        else:
            answer += 1
            if now == (location):
                return answer
    return answer

print(solution([2, 1, 3, 2],2))
