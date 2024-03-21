MOD = 10**9 + 7

# 이항계수 계산을 위한 팩토리얼과 역원 계산
factorial = [1] * 500001
inverse = [1] * 500001

for i in range(1, 500001):
    factorial[i] = factorial[i-1] * i % MOD

inverse[500000] = pow(factorial[500000], -1, MOD)
for i in range(499999, 0, -1):
    inverse[i] = inverse[i+1] * (i+1) % MOD

# 이항계수 계산
def comb(n, k):
    if n < k:
        return 0
    return factorial[n] * inverse[k] * inverse[n-k] % MOD

# 행렬식 계산
def determinant(a):
    N = len(a)
    det = 1
    for i in range(N):
        det = det * comb(a[i], i) % MOD
    return det

# 테스트
Q = int(input())
queries = []
for _ in range(Q):
    N = int(input().strip())
    a = list(map(int, input().split()))
    queries.append((N, a))
results = []

for N, a in queries:
    results.append(determinant(a))
    
print(results)
