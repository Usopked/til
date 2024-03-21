from itertools import combinations
def solve(N, weights, graph):
    nodes = range(N)
    min_difference = float('inf')
    for r in range(1, N // 2 + 1):
        for group1 in combinations(nodes, r):
            group1 = set(group1)
            group2 = set(nodes) - group1
            if is_connected(group1, graph) and is_connected(group2, graph):
                diff = abs(sum(weights[node] for node in group1) - sum(weights[node] for node in group2))
                min_difference = min(min_difference, diff)
    return min_difference
def is_connected(group, graph):
    group = set(group) 
    start = next(iter(group)) 
    visited = set([start])
    stack = [start]

    while stack:
        node = stack.pop()
        for neighbor in graph[node]:
            if neighbor in group and neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)
    return group == visited
N = int(input())
weights = list(map(int, input().split()))
graph = [list(map(int, input().split())) for _ in range(N)]
result = [[x - 1 for x in sup[1:]] for sup in graph]
ans = solve(N, weights, result)
if ans == float('inf'): print('-1')
else: print(ans)