# https://school.programmers.co.kr/learn/courses/30/lessons/42586
def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        count = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        
        if count > 0:
            answer.append(count)

    return answer
print(solution([93, 30, 55],[1, 30, 5]))