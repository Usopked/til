from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def find_farthest_vertex(start, graph):
    visited = set()
    queue = deque([(start, 0)])  # (vertex, distance)
    farthest_vertex, max_distance = start, 0

    while queue:
        current_vertex, current_distance = queue.popleft()

        if current_distance > max_distance:
            farthest_vertex, max_distance = current_vertex, current_distance

        visited.add(current_vertex)

        for neighbor, distance in graph[current_vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, current_distance + distance))
                
    return farthest_vertex, max_distance

def tree_diameter(V, edges):
    graph = defaultdict(list)

    for edge in edges:
        u = edge[0]
        for i in range(1, len(edge)-1, 2):
            v, w = edge[i], edge[i+1]
            graph[u].append((v, w))

    # Step 1: Find the farthest vertex from a random vertex (we choose 1)
    farthest_vertex, _ = find_farthest_vertex(1, graph)

    # Step 2: Find the farthest vertex from the previously found vertex to get the diameter
    _, diameter = find_farthest_vertex(farthest_vertex, graph)

    return diameter

# Sample Input
V = int(input())
edges = [list(map(int, input().split())) for _ in range(V)]

print(tree_diameter(V, edges))
