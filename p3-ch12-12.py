
def insert(result,x,y,a):
    if a == 0: # 기둥일때
        for i in range(len(result)):
            if y == 0 or (result[i][2] == 1 and (result[i][0] == x - 1 or result[i][0] == x)and result[i][1] == y) or (result[i][2] == 0 and result[i][0] == x and result[i][1] == y - 1):
                result.append([x][y][a])
    else: # 보일때
        for i in range(len(result)):
            if (result[i][2] == 0 and (result[i][0] == x or result[i][0] == x + 1) and result[i][1] == y - 1) or (result[i][2] == 1 and result[i][0] == x and result[i][0] == x + 1):
                result.append([x][y][a])
def delete(result,x,y,a):
    result.remove([x,y,a])
    return

def solution(n, build_frame):
    result = []
    answer = []

    if build_frame[3] == 1: # 건설
        insert(result,build_frame[0],build_frame[1],build_frame[2])
    else: # 삭제
        delete(result,build_frame[0],build_frame[1],build_frame[2])
    
    return result

# 정답풀이

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                continue
            return False
    return True

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        if operate == 0:
            answer.remove([x,y,stuff])
            if not possible(answer):
                answer.append([x,y,stuff])
        if operate == 1:
            answer.append([x,y,stuff])
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)