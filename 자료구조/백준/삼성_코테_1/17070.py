import sys

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1  # 초기 파이프 상태 설정

for x in range(2, N):
    if not house[0][x]:  # 벽이 없으면
        dp[0][x][0] = dp[0][x-1][0]  # 이전 위치의 가로 파이프 상태 복사

for y in range(1, N):
    for x in range(1, N):
        if not house[y][x] and not house[y][x-1] and not house[y-1][x]:  # 대각선 이동 가능하면
            dp[y][x][2] = sum(dp[y-1][x-1])  # 이전 위치의 모든 파이프 상태 복사
        if not house[y][x]:  # 벽이 없으면
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]  # 이전 위치의 가로, 대각선 파이프 상태 복사
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]  # 이전 위치의 세로, 대각선 파이프 상태 복사

print(sum(dp[N-1][N-1]))  # 최종 위치의 모든 파이프 상태 합 출력
