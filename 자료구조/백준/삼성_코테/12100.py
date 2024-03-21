from copy import deepcopy

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # right, left, down, up
result = 0


def move(board, direction):
    new_board = [[0] * N for _ in range(N)]
    if direction in [0, 2]:  # right or down
        getter = reversed
    else:
        getter = list

    for i in getter(range(N)):
        for j in getter(range(N)):
            if board[i][j] == 0:
                continue
            x, y = i, j
            while True:
                nx, ny = x + directions[direction][0], y + directions[direction][1]
                if nx < 0 or nx >= N or ny < 0 or ny >= N or new_board[nx][ny] != 0:
                    break
                x, y = nx, ny
            if new_board[x][y] == 0:
                new_board[x][y] = board[i][j]
            elif new_board[x][y] == board[i][j]:
                new_board[x][y] *= 2
                x -= directions[direction][0]
                y -= directions[direction][1]
                if x >= 0 and y >= 0:
                    new_board[x][y] = board[i][j]
    return new_board


def dfs(board, count):
    global result
    if count == 5:
        for row in board:
            result = max(result, max(row))
        return
    for direction in range(4):
        dfs(move(board, direction), count + 1)


dfs(board, 0)
print(result)
