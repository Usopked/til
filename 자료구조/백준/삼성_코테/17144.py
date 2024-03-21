import sys

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def spread():
    temp = [[0]*C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] > 0:
                cnt = 0
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != -1:
                        temp[nx][ny] += board[x][y] // 5
                        cnt += 1
                board[x][y] -= (board[x][y] // 5) * cnt
    for i in range(R):
        for j in range(C):
            board[i][j] += temp[i][j]

def purify():
    # 위쪽 반시계 방향 순환
    for i in range(purifier[0]-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(C-1):
        board[0][i] = board[0][i+1]
    for i in range(purifier[0]):
        board[i][C-1] = board[i+1][C-1]
    for i in range(C-1, 1, -1):
        board[purifier[0]][i] = board[purifier[0]][i-1]
    board[purifier[0]][1] = 0

    # 아래쪽 시계 방향 순환
    for i in range(purifier[1]+1, R-1):
        board[i][0] = board[i+1][0]
    for i in range(C-1):
        board[R-1][i] = board[R-1][i+1]
    for i in range(R-1, purifier[1], -1):
        board[i][C-1] = board[i-1][C-1]
    for i in range(C-1, 1, -1):
        board[purifier[1]][i] = board[purifier[1]][i-1]
    board[purifier[1]][1] = 0

R, C, T = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(R)]

purifier = []
for i in range(R):
    if board[i][0] == -1:
        purifier.append(i)

for _ in range(T):
    spread()
    purify()

dust = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            dust += board[i][j]

print(dust)
