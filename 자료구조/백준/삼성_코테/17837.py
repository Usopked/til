def reverse_dir(d):
    if d == 0 or d == 2:
        return d+1
    else:
        return d-1

def move(i):
    x, y, d = horses[i]
    nx, ny = x+dx[d], y+dy[d]

    # 체스판을 벗어나거나 파란색인 경우
    if nx < 0 or nx >= N or ny < 0 or ny >= N or color[nx][ny] == 2:
        nd = reverse_dir(d)
        horses[i][2] = nd
        nx, ny = x+dx[nd], y+dy[nd]
        if nx < 0 or nx >= N or ny < 0 or ny >= N or color[nx][ny] == 2:
            return 0

    if color[nx][ny] == 1:
        bottom = chess[x][y][:chess[x][y].index(i)]
        top = chess[x][y][chess[x][y].index(i):][::-1]
        chess[x][y] = bottom
        chess[nx][ny] += top
    else:
        bottom = chess[x][y][:chess[x][y].index(i)]
        top = chess[x][y][chess[x][y].index(i):]
        chess[x][y] = bottom
        chess[nx][ny] += top

    for j in chess[nx][ny]:
        horses[j][0], horses[j][1] = nx, ny

    if len(chess[nx][ny]) >= 4:
        return 1
    return 0

N, K = map(int, input().split())
color = [list(map(int, input().split())) for _ in range(N)]
chess = [[[] for _ in range(N)] for _ in range(N)]
horses = [list(map(int, input().split())) for _ in range(K)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(K):
    x, y, d = horses[i]
    horses[i][0], horses[i][1], horses[i][2] = x-1, y-1, d-1
    chess[x-1][y-1].append(i)

for t in range(1, 1001):
    for i in range(K):
        flag = move(i)
        if flag:
            print(t)
            exit(0)
print(-1)
