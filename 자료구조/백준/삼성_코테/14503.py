'''청소기 문제
공간이 주어짐(n m)
청소기 작동원리
청소 실행

1. 공간과 로봇의 방향을 설정
2. 로봇의 행동을 규정
    1. 청소 X -> 청소 , 변수 +=1
    2. 청소 O -> 주위 확인
        1. 주위 더러움 -> 반시계 방향으로 회전 후 전진
        2. 주위 깨끗함 -> 한칸 후진
3. 청소하는 칸을 출력'''

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # north, east, south, west

def solve():
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    while True:
        if room[r][c] == 0:  # if current location is dirty
            room[r][c] = 2  # clean it
            cnt += 1
        if all(room[r+dx[i]][c+dy[i]] != 0 for i in range(4)):  # check all directions
            if room[r-dx[d]][c-dy[d]] == 1:  # if backward is blocked
                break
            else:  # if backward is not blocked
                r, c = r-dx[d], c-dy[d]  # move backward
        else:  # if there are still dirty places
            d = (d+3) % 4  # rotate counterclockwise
            if room[r+dx[d]][c+dy[d]] == 0:  # if front is dirty
                r, c = r+dx[d], c+dy[d]  # move forward
    print(cnt)

solve()
