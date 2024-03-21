N = int(input())
board = [[0]*101 for _ in range(101)]
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1] # right, up, left, down

def generate_curve(x, y, d, g):
    curve = [d]
    for _ in range(g):
        curve += [(i+1)%4 for i in curve[::-1]] # change this line
    return curve

for _ in range(N):
    x, y, d, g = map(int, input().split())
    curve = generate_curve(x, y, d, g)
    board[y][x] = 1
    for direction in curve:
        x, y = x + dx[direction], y + dy[direction]
        if x < 0 or x > 100 or y < 0 or y > 100:
            continue
        board[y][x] = 1

count = 0
for i in range(100):
    for j in range(100):
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1]:
            count += 1

print(count)
