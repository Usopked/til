MOD = 1000000007
max_n = 1000000  
factorial = [1] * (max_n + 1)
inverse_factorial = [1] * (max_n + 1)

for i in range(1, max_n + 1):
    factorial[i] = (factorial[i - 1] * i) % MOD

inverse_factorial[max_n] = pow(factorial[max_n], MOD - 2, MOD)
for i in range(max_n - 1, 0, -1):
    inverse_factorial[i] = (inverse_factorial[i + 1] * (i + 1)) % MOD
def nCr(n, r):
    if r > n or r < 0 or n > max_n or r > max_n or (n - r) > max_n:
        return 0
    return (factorial[n] * inverse_factorial[r] * inverse_factorial[n - r]) % MOD

def count_paths(N, M, bombs):
    total_paths = nCr(N + M, N)
    
    for bomb in bombs:
        bx, by = bomb
        paths_through_bomb = nCr(bx + by, bx) * nCr(N + M - bx - by, N - bx)
        total_paths -= paths_through_bomb
        total_paths %= MOD
    
    return total_paths

N, M, K = map(int, input().split())
bombs = [tuple(map(int, input().split())) for _ in range(K)]
print(count_paths(N, M, bombs))
