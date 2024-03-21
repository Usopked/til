'''
브루트포스 + BFS 알고리즘
best는 기계의 시점에서 문제를 분석하고 해석하는 것
하지만 그렇게까지 할 필요는 없음..
사람이 보는 시선에서 문제를 분석한 후, 각종 알고리즘을 통해
문제해결에 적용하는 것이 포인트
'''

from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def move(i, j, dx, dy):
    c = 0 
    while board[i+dx][j+dy] != '#' and board[i][j] != 'O':
        i += dx
        j += dy
        c += 1
    return i, j, c

def bfs(rx, ry, bx, by):
    visited = [[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    queue = deque([(rx, ry, bx, by, 1)])
    visited[rx][ry][bx][by] = True
    while queue:
        rx, ry, bx, by, depth = queue.popleft()
        if depth > 10:
            break
        for i in range(4):
            nrx, nry, rc = move(rx, ry, dx[i], dy[i])
            nbx, nby, bc = move(bx, by, dx[i], dy[i])
            if board[nbx][nby] != 'O':
                if board[nrx][nry] == 'O':
                    return depth
                if nrx == nbx and nry == nby:
                    if rc > bc:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    queue.append((nrx, nry, nbx, nby, depth+1))
    return -1

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
rx, ry, bx, by = [0]*4
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

print(bfs(rx, ry, bx, by))
