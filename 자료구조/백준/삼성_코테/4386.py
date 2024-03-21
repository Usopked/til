import sys
import heapq
from math import dist

def prim():
    queue = []
    visited = [False]*n
    heapq.heappush(queue, (0, 0))  # (cost, node)
    total_cost = 0

    while queue:
        cost, node = heapq.heappop(queue)
        if not visited[node]:
            visited[node] = True
            total_cost += cost
            for next_node in range(n):
                if not visited[next_node]:
                    heapq.heappush(queue, (dist(stars[node], stars[next_node]), next_node))
    return total_cost

n = int(input())
stars = [list(map(float, sys.stdin.readline().split())) for _ in range(n)]

print(f"{prim():.2f}")
