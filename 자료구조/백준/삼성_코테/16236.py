import heapq
from collections import deque
import sys
input = sys.stdin.readline

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

def bfs(x, y, size):
    visited = [[False]*n for _ in range(n)]
    visited[x][y] = True
    eatable_fish = []
    queue = deque([(0, x, y)])

    while queue:
        dist, x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 상어보다 큰 물고기는 지나갈 수 없음
                if graph[nx][ny] > size:
                    continue
                # 물고기를 먹을 수 있는 경우
                if 0<graph[nx][ny]<size:
                    heapq.heappush(eatable_fish, (dist+1, nx, ny))
                queue.append((dist+1, nx, ny))
                visited[nx][ny] = True
    if not eatable_fish:
        return None
    return heapq.heappop(eatable_fish)


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            x, y = i, j
            graph[i][j] = 0

size = 2
exp = 0
result = 0
while True:
    tmp = bfs(x, y, size)
    if tmp is None:
        print(result)
        break
    else:
        dist, nx, ny = tmp
        result += dist
        graph[nx][ny] = 0
        exp += 1
        if exp == size:
            size += 1
            exp = 0
        x, y = nx, ny
