from collections import deque

def rotate(arr, x, d, k):
    for i in range(x-1, len(arr), x):
        arr[i].rotate(-k if d else k)

def bfs(arr, N, M):
    dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
    check = False

    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] and not visited[i][j]:
                q = deque([(i, j)])
                visited[i][j] = 1
                temp = [(i, j)]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], (y + dy[k]) % M
                        if 0 <= nx < N and arr[nx][ny] == arr[i][j] and not visited[nx][ny]:
                            visited[nx][ny] = 1
                            q.append((nx, ny))
                            temp.append((nx, ny))
                if len(temp) > 1:
                    check = True
                    for x, y in temp:
                        arr[x][y] = 0
    return check

def update(arr):
    total, cnt = 0, 0
    for row in arr:
        total += sum(row)
        cnt += len([x for x in row if x > 0])
    avg = total / cnt if cnt else 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]:
                if arr[i][j] > avg:
                    arr[i][j] -= 1
                elif arr[i][j] < avg:
                    arr[i][j] += 1

def solution():
    N, M, T = map(int, input().split())
    arr = [deque(map(int, input().split())) for _ in range(N)]
    for _ in range(T):
        x, d, k = map(int, input().split())
        rotate(arr, x, d, k)
        if not bfs(arr, N, M):
            update(arr)
    print(sum(map(sum, arr)))

solution()
