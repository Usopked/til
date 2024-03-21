#Union-Find 알고리즘

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    
    if x != y:
        parent[y] = x

n, m = map(int,input().split())
parent = [i for i in range(n+1)]

for _ in range(m):
    op, a, b = map(int,input().split())
    if op == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')
