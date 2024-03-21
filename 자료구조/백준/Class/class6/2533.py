import sys
sys.setrecursionlimit(10**6)

def dfs(node, parent):
    dp[0][node] = 0
    dp[1][node] = 1

    for child in graph[node]:
        if child == parent:
            continue
        dfs(child, node)
        
        dp[0][node] += dp[1][child]
        dp[1][node] += min(dp[0][child], dp[1][child])

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0] * (N+1) for _ in range(2)]
dfs(1, 0)
print(min(dp[0][1], dp[1][1]))
