import sys
sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline

MOD = 1_000_000_007

def matmul(A, B):
    N = len(A)
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
                result[i][j] %= MOD
    return result


def matpow(matrix, exp, N):
    if exp == 1:
        return matrix
    if exp % 2:
        half_pow = matpow(matrix, (exp-1)//2, N)
        return matmul(matmul(half_pow, half_pow), matrix)
    else:
        half_pow = matpow(matrix, exp//2, N)
        return matmul(half_pow, half_pow)
    
def create_matrix_from_map(N, map_info):
    matrix = [[0] * N for _ in range(N)]
    for info in map_info:
        a, b, c = info
        matrix[a-1][b-1] = c
    return matrix

def solve(T, N, D, maps_info):
    matrices = [create_matrix_from_map(N, map_info) for map_info in maps_info]
    identity = [[0 if i != j else 1 for j in range(N)] for i in range(N)]
    powers = [matpow(mat, D // T, N) for mat in matrices]
    for _ in range(D % T):
        powers = [matmul(powers[i], matrices[(i+1) % T]) for i in range(T)]
    result = matmul(identity, powers[0])
    for i in range(1, T):
        result = matmul(result, powers[i])
    
    return result

def get_maps_info(T, N):
    maps_info = []
    for _ in range(T):
        M = int(input())
        map_info = [list(map(int, input().split())) for _ in range(M)]
        maps_info.append(map_info)
    return maps_info

T, N, D = map(int, input().split())
maps_info =  get_maps_info(T, N)

for i in range(len(maps_info)+1):
    print(*solve(T, N, D, maps_info)[i])

