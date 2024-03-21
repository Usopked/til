from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(office, count, x, y, direction):
    i, j = x, y
    while True:
        nx = i + dx[direction]
        ny = j + dy[direction]
        if nx < 0 or ny < 0 or nx >= n or ny >= m:
            break
        if office[nx][ny] == 6:
            break
        if office[nx][ny] == 0:
            office[nx][ny] = "#"
        i, j = nx, ny

def dfs(office, cctvs, count, idx):
    global ans
    temp = deepcopy(office)
    if idx == count:
        empty = 0
        for i in range(n):
            empty += temp[i].count(0)
        ans = min(ans, empty)
        return
    x, y, cctv = cctvs[idx]
    for dir in directions[cctv]:
        for d in dir:
            check(temp, count, x, y, d)
        dfs(temp, cctvs, count, idx + 1)
        temp = deepcopy(office)

n, m = map(int, input().split())
office = []
cctvs = []
count = 0
directions = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [3, 0]],
    [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    [[0, 1, 2, 3]]
]
for i in range(n):
    row = list(map(int, input().split()))
    office.append(row)
    for j in range(m):
        if row[j] != 0 and row[j] != 6:
            cctvs.append([i, j, row[j]])
            count += 1
ans = float('inf')
dfs(office, cctvs, count, 0)
print(ans)
