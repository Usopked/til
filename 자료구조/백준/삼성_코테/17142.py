   
from itertools import combinations
from collections import deque

N,M = map(int, input().split())
arr=[list(map(int, input().split())) for _ in range(N)]
    
virus = []
V = 0
K = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            virus.append((i, j))
            V += 1
        elif arr[i][j] == 0:
            K += 1
ans = float('inf')

def bfs(distance, res):
    global ans
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # up, down, left, right
    Q = deque(res)
    for r in res:
        distance[r[0]][r[1]] = 0
    t = infected = 0
    while Q:
        idxs = Q.popleft()
        for dr, dc in zip(dx, dy):
            nr = idxs[0] + dr
            nc = idxs[1] + dc
            if 0 <= nr < N and 0 <= nc < N and distance[nr][nc] == -1 and arr[nr][nc] != 1:
                distance[nr][nc] = distance[idxs[0]][idxs[1]] + 1
                Q.append((nr, nc))
                if arr[nr][nc] == 0:
                    infected += 1
                    t = distance[nr][nc]
    if K == infected:
        ans = min(ans, t)

for comb in combinations(range(V), M):
    distance = [[-1] * N for _ in range(N)]
    res = [virus[i] for i in comb]
    bfs(distance, res)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
