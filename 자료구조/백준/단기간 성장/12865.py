n, k = map(int, input().split())
items = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = items[i][0]  # 현재 물품의 무게
        value = items[i][1]   # 현재 물품의 가치

        if j < weight:
            # 현재 가방의 용량(j)가 현재 물품의 무게보다 작을 경우
            # 이전 물품까지의 최적의 해(dp[i-1][j])를 그대로 가져옴
            dp[i][j] = dp[i-1][j]
        else:
            # 현재 물품을 가방에 넣는 경우와 넣지 않는 경우 중 가치가 더 높은 경우를 선택
            dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])

print(dp[n][k])
