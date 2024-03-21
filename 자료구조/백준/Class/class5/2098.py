def TSP(N, W):
    INF = float('inf')
    # dp[mask][i] : mask 상태에서 마지막 방문 도시가 i일 때의 최소 비용
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1][0] = 0  # 시작 도시는 항상 0번 도시

    for mask in range(1, 1 << N):
        for i in range(N):
            # 현재 상태에서 i번 도시를 방문하지 않았거나, i가 마지막 방문 도시가 아닌 경우 건너뜀
            if not (mask & (1 << i)) or not dp[mask][i] < INF:
                continue

            for j in range(N):
                # j번 도시를 이미 방문했거나 i에서 j로의 경로가 없는 경우 건너뜀
                if mask & (1 << j) or W[i][j] == 0:
                    continue

                next_mask = mask | (1 << j)
                dp[next_mask][j] = min(dp[next_mask][j], dp[mask][i] + W[i][j])

    # 모든 도시를 방문한 상태에서 다시 0번 도시로 돌아가는 비용 계산
    min_cost = INF
    for i in range(1, N):
        if W[i][0] != 0:
            min_cost = min(min_cost, dp[(1 << N) - 1][i] + W[i][0])

    return min_cost

# 예제 입력
N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

print(TSP(N, W))
