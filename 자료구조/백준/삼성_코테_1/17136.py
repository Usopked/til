import sys

def dfs(x, y, cnt):
    global ans
    if y == 10:
        dfs(x+1, 0, cnt)
        return
    if x == 10:
        ans = min(ans, cnt)
        return
    if arr[x][y] == 0:
        dfs(x, y+1, cnt)
        return
    for k in range(5, 0, -1):
        if paper[k] == 0 or x + k > 10 or y + k > 10:
            continue
        if check(x, y, k):
            set_paper(x, y, k, 0)
            paper[k] -= 1
            dfs(x, y+1, cnt+1)
            set_paper(x, y, k, 1)
            paper[k] += 1

def check(x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            if arr[i][j] == 0:
                return False
    return True

def set_paper(x, y, k, num):
    for i in range(x, x+k):
        for j in range(y, y+k):
            arr[i][j] = num

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
ans = float('inf')
dfs(0, 0, 0)

if ans == float('inf'):
    print(-1)
else:
    print(ans)
