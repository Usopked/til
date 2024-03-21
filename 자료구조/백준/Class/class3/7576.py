from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
queue = deque([(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
days = -1

while queue:
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
                grid[nx][ny] = 1
                queue.append((nx, ny))
    days += 1

# 모든 토마토가 익었는지, 또는 토마토가 없는 칸이 있는지 확인
for i in range(n):
    for j in range(m):
        if grid[i][j] == 0:
            print(-1)
            exit(0)

print(days)
