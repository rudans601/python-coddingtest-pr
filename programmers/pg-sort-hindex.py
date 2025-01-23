def solution(citations):
    length = len(citations)
    citations.sort(reverse=True)
    answer = 0
    for i in range(length):
        if citations[i] >= i+1:
            answer = i+1
    return answer

print(solution([3,0,6,1,5]))
