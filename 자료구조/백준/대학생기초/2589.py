from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
#x축과 y축의 이동으로 0부터 3까지의 수에 왼쪽, 오른쪽, 위, 아래라는 성질을 부여함


def bfs(x, y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if a[nx][ny] == 'L' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = visited[x][y] + 1
    return visited[x][y] - 1

n, m = map(int, input().split())
a = [list(input().strip()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == 'L':
            result = max(result, bfs(i, j))
print(result)
