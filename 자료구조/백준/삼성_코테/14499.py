N, M, x, y, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

# 주사위를 표현하는 리스트입니다. 초기에는 모든 면이 0입니다.
dice = [0] * 6

# 각 명령에 따른 주사위의 변화를 표현하는 룰입니다.
# 각 튜플의 인덱스는 주사위의 면을 나타내고, 해당 위치의 값은 명령 후에 그 면으로 올라오는 주사위 면입니다.
change = [
    (3, 1, 0, 5, 4, 2),  # 동쪽으로 굴릴 때
    (2, 1, 5, 0, 4, 3),  # 서쪽으로 굴릴 때
    (4, 0, 2, 3, 5, 1),  # 북쪽으로 굴릴 때
    (1, 5, 2, 3, 0, 4)   # 남쪽으로 굴릴 때
]

# 각 명령에 따른 주사위의 위치 변화입니다.
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for command in commands:
    nx, ny = x + dx[command-1], y + dy[command-1]

    # 만약 새 위치가 지도 밖이라면 무시하고 다음 명령으로 넘어갑니다.
    if not (0 <= nx < N and 0 <= ny < M):
        continue

    # 주사위를 굴립니다.
    dice = [dice[i] for i in change[command-1]]

    if board[nx][ny] == 0:
        # 새 위치에 쓰여 있는 수가 0이라면 주사위 바닥면의 수를 복사합니다.
        board[nx][ny] = dice[5]
    else:
        # 새 위치에 쓰여 있는 수가 0이 아니라면 그 수를 주사위 바닥면에 복사하고, 새 위치의 수를 0으로 만듭니다.
        dice[5] = board[nx][ny]
        board[nx][ny] = 0

    # 주사위의 윗면을 출력합니다.
    print(dice[0])

    x, y = nx, ny  # 주사위의 위치를 업데이트합니다.
