MOD = 1_000_000_000

def count_stair_numbers(N):
    dp = [[[0] * 1024 for _ in range(10)] for _ in range(N+1)]
    for i in range(1, 10):
        dp[1][i][1 << i] = 1

    for i in range(2, N+1):
        for j in range(10):
            for k in range(1024):
                if j > 0:
                    dp[i][j][k | (1 << j)] += dp[i-1][j-1][k]
                if j < 9:
                    dp[i][j][k | (1 << j)] += dp[i-1][j+1][k]
                
                dp[i][j][k | (1 << j)] %= MOD

    return sum(dp[N][i][1023] for i in range(10)) % MOD


N = int(input())
print(count_stair_numbers(N))
