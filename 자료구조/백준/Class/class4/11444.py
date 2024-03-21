def mat_mult(A, B, mod):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod for j in range(len(B[0]))] for i in range(len(A))]

def mat_pow(A, p, mod):
    if p == 1:
        return A
    if p % 2:
        return mat_mult(A, mat_pow(A, p - 1, mod), mod)
    half_pow = mat_pow(A, p // 2, mod)
    return mat_mult(half_pow, half_pow, mod)

def fibonacci(n, mod):
    if n <= 1:
        return n
    F = [[1, 1], [1, 0]]
    result_mat = mat_pow(F, n - 1, mod)
    return result_mat[0][0]

n = int(input())
mod = 1_000_000_007
result = fibonacci(n, mod)
print(result)
