from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, y, x, visited):
    color = board[y][x]
    queue = deque([(y, x)])
    group = [(y, x)]
    visited[y][x] = True

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 6 and 0 <= ny < 12 and not visited[ny][nx] and board[ny][nx] == color:
                queue.append((ny, nx))
                group.append((ny, nx))
                visited[ny][nx] = True

    return group

def gravity(board):
    for x in range(6):
        puyo = [board[y][x] for y in range(12) if board[y][x] != '.']
        puyo = ['.'] * (12 - len(puyo)) + puyo
        for y in range(12):
            board[y][x] = puyo[y]

def solution(board):
    chain = 0
    while True:
        visited = [[False]*6 for _ in range(12)]
        groups = []
        for y in range(12):
            for x in range(6):
                if board[y][x] != '.' and not visited[y][x]:
                    group = bfs(board, y, x, visited)
                    if len(group) >= 4:
                        groups.append(group)

        if not groups:
            break

        for group in groups:
            for y, x in group:
                board[y][x] = '.'
        gravity(board)
        chain += 1

    return chain

# test the function

board = [list(input()) for _ in range(12)]

print(solution(board))
