def solve(N, M, paper):
    tetromino = [[(0,0),(0,1),(0,2),(0,3)],\
        [(0,0),(1,0),(2,0),(3,0)],\
        [(0,0),(1,0),(0,1),(1,1)],\
        [(0,0),(1,0),(2,0),(2,1)],\
        [(0,1),(1,1),(2,1),(2,0)],\
        [(0,0),(0,1),(1,1),(2,1)],\
        [(0,0),(0,1),(1,0),(2,0)],\
        [(0,0),(1,0),(1,1),(1,2)],\
        [(0,2),(1,1),(1,2),(1,0)],\
        [(0,0),(0,1),(0,2),(1,2)],\
        [(0,0),(1,0),(0,1),(0,2)],\
        [(0,0),(1,0),(1,1),(2,1)],\
        [(0,1),(1,1),(1,0),(2,0)],\
        [(1,0),(1,1),(0,1),(0,2)],\
        [(0,0),(0,1),(1,1),(1,2)],\
        [(0,1),(1,0),(1,1),(1,2)],\
        [(0,0),(0,1),(0,2),(1,1)],\
        [(0,0),(1,0),(1,1),(2,0)],\
        [(0,1),(1,1),(1,0),(2,1)]]

    max_val = 0
    for i in range(N):
        for j in range(M):
            for t in tetromino:
                try:
                    if all(0 <= i + ti < N and 0 <= j + tj < M for ti, tj in t):
                        sum_val = sum(paper[i + ti][j + tj] for ti, tj in t)
                        max_val = max(max_val, sum_val)
                except IndexError:
                    continue
    return max_val
N, M = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(N)]

print(solve(N, M, paper))