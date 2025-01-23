#https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = []
    i = 0
    while i < len(arr):
        answer.append(arr[i])
        j = i
        while j < len(arr) - 1 and arr[j] == arr[j + 1]:
            j += 1
        i = j + 1
    return answer

print(solution([1, 1, 3, 3, 0, 1, 1]))