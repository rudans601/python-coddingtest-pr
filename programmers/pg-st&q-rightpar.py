# https://school.programmers.co.kr/learn/courses/30/lessons/12909
from collections import deque
def solution(s):
    queue = deque()
    ss = deque(s)
    while len(ss) > 0:
        now = ss.popleft()
        print("ss",ss)
        if now == "(":
            queue.append(now)
            print("que",queue)
        else:
            if queue and queue[0] == "(":
                queue.popleft()
                print("que",queue)
            else:
                return False
    
    if queue:
        return False
    else:
        return True

print(solution(")()("))