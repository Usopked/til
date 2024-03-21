from collections import deque
import sys

# 입력 받기
m, n, h = map(int, sys.stdin.readline().split())
boxes = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

queue = deque([(i, j, k) for i in range(h) for j in range(n) for k in range(m) if boxes[i][j][k] == 1])

# 상하좌우 위아래로 움직이기 위한 리스트
dx = [-1, 0, 1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

days = -1

while queue:
    for _ in range(len(queue)):
        z, x, y = queue.popleft()
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and boxes[nz][nx][ny] == 0:
                boxes[nz][nx][ny] = 1
                queue.append((nz, nx, ny))
    days += 1

# 모든 토마토가 익었는지 확인
for i in range(h):
    for j in range(n):
        for k in range(m):
            if boxes[i][j][k] == 0:
                print(-1)
                exit(0)

print(days)
