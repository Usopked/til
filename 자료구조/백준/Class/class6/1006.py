#로직에 이상무
#몇몇 케이스를 고려하지 못하고 있음
import sys
#sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline

def min_forces(N, w, e):
    flat_e = e[0] + e[1]
    
    def generate_combinations(i):
        adj = [i - 1, (i + 1) % (2 * N), (i + N) % (2 * N)]
        combinations = []
        if flat_e[i] <= w:
            combinations.append([i])
        for j in adj:
            if flat_e[i] + flat_e[j] <= w:
                combinations.append(sorted([i, j]))
        return combinations
    
    dp = [float('inf')] * (2 * N + 1)
    dp[0] = 0
    for i in range(2 * N):
        for comb in generate_combinations(i):
            prev = max(comb) - len(comb) + 1
            dp[max(comb) + 1] = min(dp[max(comb) + 1], dp[prev] + 1)
    return dp[2 * N]

cnt = int(input())
for _ in range(cnt):
    N, w = map(int, input().split())
    e = [list(map(int, input().split())) for _ in range(2)]
    print(min_forces(N, w, e))