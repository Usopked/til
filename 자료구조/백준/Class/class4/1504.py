import heapq

def dijkstra(start, graph):
    distance = [float('inf')] * (len(graph))
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        curr_distance, curr_vertex = heapq.heappop(queue)
        
        for neighbor, weight in graph[curr_vertex]:
            new_distance = curr_distance + weight
            # Check if the new distance is shorter
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(queue, (new_distance, neighbor))
                
    return distance

def min_distance_through_AB(N, graph, A, B):
    distance_from_1 = dijkstra(1, graph)
    distance_from_A = dijkstra(A, graph)
    distance_from_B = dijkstra(B, graph)

    path_1_A_B_N = distance_from_1[A] + distance_from_A[B] + distance_from_B[N]
    path_1_B_A_N = distance_from_1[B] + distance_from_B[A] + distance_from_A[N]

    if path_1_A_B_N == float('inf') and path_1_B_A_N == float('inf'):
        return -1

    return min(path_1_A_B_N, path_1_B_A_N)

def create_adj_list_from_edges(edges, N):
    graph = [[] for _ in range(N + 1)]  # Assuming vertices are 1-indexed
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))  # For bidirectional graph
    return graph

N, M = map(int, input().split())
a = [tuple(map(int, input().split())) for _ in range(M)]
graph = create_adj_list_from_edges(a, N)
A, B = map(int, input().split())
print(min_distance_through_AB(N, graph, A, B))