from itertools import combinations

def check(candidates):
    for start in range(N):
        k = start
        for i in range(H):
            if board[i][k]:
                k += 1
            elif k > 0 and board[i][k-1]:
                k -= 1
        if start != k:
            return False
    return True

def solve():
    for cnt in range(4):
        for combi in combinations(candidates, cnt):
            for x, y in combi:
                board[x][y] = True
            if check(candidates):
                return cnt
            for x, y in combi:
                board[x][y] = False
    return -1

N, M, H = map(int, input().split())
board = [[False]*N for _ in range(H)]
candidates = [(i, j) for i in range(H) for j in range(N-1)]

if M:
    lines = [list(map(int, input().split())) for _ in range(M)]
    for x, y in lines:
        board[x-1][y-1] = True
        if (x-1, y-1) in candidates:
            candidates.remove((x-1, y-1))
        if y > 1 and (x-1, y-2) in candidates:
            candidates.remove((x-1, y-2))
        if y < N and (x-1, y) in candidates:
            candidates.remove((x-1, y))

print(solve())
