import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def max_docking_planes(G, P, planes):
    parent = [i for i in range(G + 1)]
    result = 0
    for plane in planes:
        gate = find(parent, plane)
        if gate == 0: 
            break
        union(parent, gate, gate - 1)
        result += 1
    return result

G = int(input())
P = int(input())
planes = [int(input()) for _ in range(P)]

print(max_docking_planes(G, P, planes))
