# n = int(input())
# school = []
# teach_loc = []
# student_loc = []
# object_loc = []

# for i in range(n):
#     l = list(input().split())
#     school.append(l)
#     if "S" in l:
#         student_loc.append((i,l.index("S")))
#     if "T" in l:
#         teach_loc.append((i,l.index("T")))

# def check():
#     for x,y in teach_loc:
#         for p,q in student_loc:
#             if (x == p and x not in object_loc[0]) or (y == q and y not in object_loc[1]):
#                return False
#     return True

# num = 0
# while True:
#     while num <= 3:
#         for i in range(n):
#             for j in range(n):
#                 if school[i][j] == "X":
#                     school[i][j] = "O"
#                     object_loc.append((i,j))
#                     num += 1

#     if check():
#         print("YES")
#         break
#     else:
#         if i == n - 1 and j == n - 1:
#             print("NO")
#             break
#         else:
#             object_loc.clear()
#             num = 0

# 정답풀이
from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        if board[i][j] == 'T':
            teachers.append((i,j))
        if board[i][j] == 'X':
            spaces.append((i,j))

def watch(x,y,direction):
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y -= 1
    if direction == 1:
        while y < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1
    if direction == 3:
        while x < n:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    return False

def process():
    for x,y in teachers:
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

find = False

for data in combinations(spaces, 3):
    for x,y in data:
        board[x][y] = 'O'
    if not process():
        find = True
        break
    
    for x,y in data:
        board[x][y] = 'X'

if find:
    print("YES")
else:
    print("NO")