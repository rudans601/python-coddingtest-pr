n = int(input())
k = int(input())

board = [[0] * (n+1)  for _ in range(n + 1)]
board[1][1] = 1

start = [1,1]
st_d = 0
end = [1,1]
en_d = 0
length = 1

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for i in range(k):
    x,y = map(int,input().split())
    board[x][y] = 2

l = int(input())
for i in range(l):
    x,c = input().split()
    times = 1
    for j in range(1,x+1):
        tx = start[0] + dx[st_d]
        ty = start[1] + dy[st_d]
        if tx > n or tx < 1 or ty > n or ty < 1:
            break
        if board[tx][ty] == 2:
            length += 1
            board[tx][ty] = 1
        else:
            board[tx][ty] = 1
            board[end[0]][end[1]] = 0
            end[0] += dx[en_d]
            end[1] += dy[en_d]
        times += 1
        
print(times)

# 정답 풀이
n = int(input())
k = int(input())
data = [[0] * (n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a,b = map(int,input().split())
    data[a][b] = 1

l = int(input())
for _ in range(l):
    x,c = input().split()
    info.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def turn(direction,c):
    if c == "L":
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

def simulate():
    x,y = 1,1
    data[x][y] = 2
    direction = 0
    time = 0
    index = 0
    q = [(x,y)]
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            if data[nx][ny] == 0:
                data[nx][ny] = 2
                q.append((nx,ny))
                px,py = q.pop(0)
                data[px][py] = 0
            if data[nx][ny] == 1:
                data[nx][ny] = 2
                q.append((nx,ny))
        else:
            time += 1
            break
        x,y = nx, ny
        time += 1
        if index < l and time == info[index][0]:
            direction = turn(direction,info[index][1])
            index += 1
    return time

print(simulate())