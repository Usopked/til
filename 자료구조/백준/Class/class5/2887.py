import sys
input = sys.stdin.readline
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootX] = rootY

def min_tunnel_cost(N, planets):
    edges = []
    for i in range(3):  # for x, y, z
        planets.sort(key=lambda x: x[1][i])
        for j in range(1, N):
            cost = abs(planets[j-1][1][i] - planets[j][1][i])
            edges.append((cost, planets[j-1][0], planets[j][0]))
    
    edges.sort()
    uf = UnionFind(N)
    total_cost = 0
    
    for edge in edges:
        cost, a, b = edge
        if uf.find(a) != uf.find(b):
            uf.union(a, b)
            total_cost += cost
            
    return total_cost

# Test the function
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
planets = [(i, (x, y, z)) for i, (x, y, z) in enumerate(arr)]
print(min_tunnel_cost(N, planets))
