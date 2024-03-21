import heapq

def dijkstra(start, graph):
    distance = [float('inf')] * (len(graph) + 1)
    distance[start] = 0
    queue = [(0, start)]
    
    while queue:
        curr_dist, curr_vertex = heapq.heappop(queue)
        if distance[curr_vertex] < curr_dist:
            continue
        for neighbor, weight in graph[curr_vertex]:
            if curr_dist + weight < distance[neighbor]:
                distance[neighbor] = curr_dist + weight
                heapq.heappush(queue, (distance[neighbor], neighbor))
    return distance

def max_travel_time(N, M, X, roads):
    graph = [[] for _ in range(N + 1)]
    reverse_graph = [[] for _ in range(N + 1)]

    for u, v, t in roads:
        graph[u].append((v, t))
        reverse_graph[v].append((u, t))

    # Calculate shortest paths from every city to X and from X to every city
    to_X = dijkstra(X, reverse_graph)
    from_X = dijkstra(X, graph)

    # Calculate total travel time for every student and find the maximum
    max_time = max(to_X[i] + from_X[i] for i in range(1, N + 1))
    
    return max_time

# Sample Input
N, M, X = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

# Testing the sample
print(max_travel_time(N, M, X, roads))
