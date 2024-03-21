from itertools import combinations
from copy import deepcopy
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(lab, x, y, visited):
    queue = deque([(x, y)])
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx, ny = v[0] + dx[i], v[1] + dy[i]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if lab[nx][ny] != 1:
                    visited[nx][ny] = True
                    lab[nx][ny] = 2
                    queue.append((nx, ny))

def count_area(lab):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                cnt += 1
    return cnt

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
zeros = []
viruses = []
max_area = 0

for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            zeros.append((i, j))
        elif lab[i][j] == 2:
            viruses.append((i, j))

for walls in combinations(zeros, 3):
    temp = deepcopy(lab)
    visited = [[False]*M for _ in range(N)]
    for wall in walls:
        temp[wall[0]][wall[1]] = 1
    for virus in viruses:
        bfs(temp, virus[0], virus[1], visited)
    max_area = max(max_area, count_area(temp))

print(max_area)
