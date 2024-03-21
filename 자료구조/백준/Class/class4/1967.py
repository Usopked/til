from collections import deque

def bfs(start, graph):
    visited = [-1] * (len(graph))
    queue = deque([start])
    visited[start] = 0

    while queue:
        v = queue.popleft()
        for w, cost in graph[v]:
            if visited[w] == -1:
                visited[w] = visited[v] + cost
                queue.append(w)

    return visited

def tree_diameter(n, edges):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # 1번 노드에서 가장 먼 노드 찾기
    first = bfs(1, graph)
    farthest_node = first.index(max(first))

    # 가장 먼 노드에서 다시 BFS 수행
    second = bfs(farthest_node, graph)

    return max(second)

# 예시로 테스트
n = int(input())
edges = [tuple(map(int,input().split())) for _ in range(n)]
print(tree_diameter(n, edges))
