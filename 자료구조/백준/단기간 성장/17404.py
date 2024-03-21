import sys

N = int(sys.stdin.readline())
RGB = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
INF = sys.maxsize
result = INF

for start_color in range(3):
    dp = [[0]*3 for _ in range(N)]
    for i in range(3):
        if i == start_color:
            dp[0][i] = RGB[0][i]
        else:
            dp[0][i] = INF
            
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + RGB[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + RGB[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + RGB[i][2]
        
    for i in range(3):
        if i == start_color:
            continue
        result = min(result, dp[N-1][i])

print(result)
print(dp)
