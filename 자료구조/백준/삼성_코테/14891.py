from collections import deque

# 톱니바퀴 정보 입력받기
gears = [deque(list(map(int, list(input().strip())))) for _ in range(4)]

# 각 톱니바퀴를 회전시키는 함수
def rotate(gear, direction):
    if direction == 1:
        temp = gear.pop()
        gear.appendleft(temp)
    elif direction == -1:
        temp = gear.popleft()
        gear.append(temp)

# 각 톱니바퀴를 어느 방향으로 회전시킬지 결정하는 함수
def check_rotate(gears, gear_num, direction):
    rotate_dir = [0 for _ in range(4)]
    rotate_dir[gear_num] = direction

    # 현재 톱니바퀴의 왼쪽 톱니바퀴들을 확인
    for i in range(gear_num, 0, -1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dir[i - 1] = -rotate_dir[i]
        else:
            break
    # 현재 톱니바퀴의 오른쪽 톱니바퀴들을 확인
    for i in range(gear_num, 3):
        if gears[i][2] != gears[i + 1][6]:
            rotate_dir[i + 1] = -rotate_dir[i]
        else:
            break
    return rotate_dir

# 회전 명령 입력받기
K = int(input())
for _ in range(K):
    gear_num, direction = map(int, input().split())
    gear_num -= 1  # gear_num을 인덱스 값으로 변환
    rotate_dir = check_rotate(gears, gear_num, direction)
    for i in range(4):
        rotate(gears[i], rotate_dir[i])

# 최종 점수 계산
score = 0
for i in range(4):
    score += (2 ** i) * gears[i][0]

print(score)
