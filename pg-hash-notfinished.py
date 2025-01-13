#https://school.programmers.co.kr/learn/courses/30/lessons/42576
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]

# def solution(participant, completion):
#     for data in participant:
#         if data in completion:
#             participant.remove(data)
#             completion.remove(data)
#     return participant.pop()

# print(solution(participant, completion))

# 정답 풀이
def solution(participant, completion):
    hash ={}
    for i in participant:
        if i in hash:
            hash[i] += 1
        else:
            hash[i] = 1
    for i in completion:
        if hash[i] == 1:
            del hash[i]
        else:
            hash[i] -= 1
    answer = list(hash.keys())[0]
    return answer