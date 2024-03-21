import heapq

def dijkstra(V, E, K, edges):
    # 그래프 초기화
    graph = [[] for _ in range(V + 1)]
    for edge in edges:
        u, v, w = edge
        graph[u].append((v, w))
    
    # 거리 초기화
    INF = float('inf')
    distance = [INF] * (V + 1)
    distance[K] = 0

    # 우선순위 큐 사용
    q = []
    heapq.heappush(q, (0, K)) # (거리, 정점)

    while q:
        dist, current_vertex = heapq.heappop(q)

        # 이미 처리된 정점은 무시
        if distance[current_vertex] < dist:
            continue
        
        for i in graph[current_vertex]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 시작점은 0, 나머지는 거리값 또는 INF
    result = ['0' if distance[i] == 0 else str(distance[i]) if distance[i] != INF else 'INF' for i in range(1, V + 1)]
    
    return result

# 예시로 테스트
V, E = map(int, input().split())
K = int(input())
edges = [tuple(map(int, input().split())) for _ in range(E)]
for i in dijkstra(V, E, K, edges):
    print(i)
