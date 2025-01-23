# from itertools import permutations

# def solution(numbers):
#     answer = []
#     per_list = list(permutations(numbers,len(numbers)))
#     for i in per_list:
#         str1 = ''
#         for j in i:
#             str1 += str(j)
#         answer.append(int(str1))
#     answer.sort()
#     return str(answer[-1])
        
        
# print(solution([6,10,2]))
# 정답이지만 특정 케이스 시간 초과...
# 해답코드
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    answer = ''.join(numbers)
    return '0' if answer[0] == '0' else answer