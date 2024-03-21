import sys
sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline

from collections import deque, defaultdict

def meet_time_and_roads(n, m, roads, start, end):
    graph = defaultdict(list)
    indegrees = [0] * (n + 1)
    for u, v, w in roads:
        graph[u].append((v, w))
        indegrees[v] += 1
    q = deque()
    for i in range(1, n + 1):
        if indegrees[i] == 0:
            q.append(i)
    
    topo_order = []
    while q:
        node = q.popleft()
        topo_order.append(node)
        for v, _ in graph[node]:
            indegrees[v] -= 1
            if indegrees[v] == 0:
                q.append(v)
    
    dist = [float('-inf')] * (n + 1)
    dist[start] = 0
    edge_used = defaultdict(int)
    
    for node in topo_order:
        for v, w in graph[node]:
            if dist[v] < dist[node] + w:
                dist[v] = dist[node] + w
                edge_used[(node, v)] = 1  

    max_time = dist[end]

    count = sum(1 for key in edge_used if edge_used[key] == 1)

    return max_time, count

# Test
n = int(input())
m = int(input())
roads = [tuple(map(int, input().split())) for _ in range(m)]
start, end = map(int, input().split())
print(*meet_time_and_roads(n, m, roads, start, end), sep='\n')
