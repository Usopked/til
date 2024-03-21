from sys import stdin

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(stdin.readline())
board = [[0] * N for _ in range(N)]
student_dict = dict()
order = []

# 각 학생의 정보를 입력받습니다.
for _ in range(N*N):
    info = list(map(int, stdin.readline().split()))
    student_dict[info[0]] = info[1:]
    order.append(info[0])

for student in order:
    like = student_dict[student]
    max_like = -1
    max_empty = -1
    position = [-1, -1]

    for x in range(N):
        for y in range(N):
            if board[x][y] == 0:
                like_count = 0
                empty_count = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] in like:
                            like_count += 1
                        if board[nx][ny] == 0:
                            empty_count += 1
                if like_count > max_like or (like_count == max_like and empty_count > max_empty):
                    position = [x, y]
                    max_like = like_count
                    max_empty = empty_count
    board[position[0]][position[1]] = student

answer = 0
for x in range(N):
    for y in range(N):
        count = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] in student_dict[board[x][y]]:
                count += 1
        if count != 0:
            answer += 10 ** (count - 1)
print(answer)
