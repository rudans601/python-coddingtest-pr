#https://school.programmers.co.kr/learn/courses/30/lessons/42577

# phone_book = ["12","1235","123","567","88"]
# phone_book.sort(key=int)

# for i in range(len(phone_book)-1):
#     for j in range(i+1):
#         for k in range(len(i)):
#             if phone_book[i][k] != phone_book[j][k]:
#                 break

# 모르겠다
# 정답 코드
def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]:
            return False
    return True