N = 5
stages = [4,2,3,1,5]
answer = [[0,0] for _ in range(N+1)] #스테이지에 도달, 클리어 못함/스테이지 도달 플레이어

stages.sort()

# 정답 풀이
def solution(N, stages):
    answer = []
    length = len(stages)
    
    for i in range(1,N+1):
        count = stages.count(i)
        
        if length == 0:
            fail = 0
        else:
            fail = count / length
            
        answer.append((i,fail))
        length -= count
    answer = sorted(answer,key=lambda t: t[1], reverse= True)
    
    answer = [i[0] for i in answer]
    return answer