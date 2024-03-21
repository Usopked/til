import sys

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

DP = [[0] * N for _ in range(N)]

for i in range(N):
    DP[i][i] = 1

for i in range(N - 1):
    if numbers[i] == numbers[i + 1]:
        DP[i][i + 1] = 1

for i in range(2, N):
    for j in range(N - i):
        if numbers[j] == numbers[j + i] and DP[j + 1][j + i - 1] == 1:
            DP[j][j + i] = 1

M = int(sys.stdin.readline())
for _ in range(M):
    S, E = map(int, sys.stdin.readline().split())
    print(DP[S - 1][E - 1])