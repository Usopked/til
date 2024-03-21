'''R, C, M = map(int, input().split())
shark = [list(map(int, input().split())) for _ in range(M)]
board = [[0]*R for _ in range(C)]

for i in shark:
    board[i[1]][i[0]] = 1

man = 
while R:
'''

# 상어 낚시를 시뮬레이션하는 함수
def fishing_simulation(R, C, M, sharks):
    # 상어의 이동 방향에 따른 좌표 변화 (위, 아래, 오른쪽, 왼쪽)
    directions = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
    
    # 격자판 초기화
    grid = [[None] * C for _ in range(R)]
    for shark in sharks:
        r, c, s, d, z = shark
        grid[r-1][c-1] = shark
    
    # 낚시왕의 위치 및 잡은 상어 크기 합
    fisherman_col = -1
    caught_shark_size = 0

    # 낚시왕의 이동
    while fisherman_col < C - 1:
        # 낚시왕의 이동
        fisherman_col += 1
        
        # 상어 잡기
        for row in range(R):
            if grid[row][fisherman_col]:
                caught_shark_size += grid[row][fisherman_col][-1]
                grid[row][fisherman_col] = None
                break
        
        # 상어 이동
        new_grid = [[None] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                shark = grid[i][j]
                if shark:
                    r, c, s, d, z = shark
                    dr, dc = directions[d]
                    for _ in range(s):
                        # 경계를 넘는 경우 방향 변경
                        if r + dr < 1 or r + dr > R or c + dc < 1 or c + dc > C:
                            # 위아래 방향 변경
                            if d == 1:
                                d = 2
                            elif d == 2:
                                d = 1
                            # 좌우 방향 변경
                            elif d == 3:
                                d = 4
                            elif d == 4:
                                d = 3
                            dr, dc = directions[d]
                        r += dr
                        c += dc
                    # 격자판에 상어 위치 갱신
                    if not new_grid[r-1][c-1] or new_grid[r-1][c-1][-1] < z:
                        new_grid[r-1][c-1] = (r, c, s, d, z)
        grid = new_grid
    
    return caught_shark_size

# 입력 받기
R, C, M = map(int, input().strip().split())
sharks = [tuple(map(int, input().strip().split())) for _ in range(M)]

# 결과 출력
result = fishing_simulation(R, C, M, sharks)
print(result)
