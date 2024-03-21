class SegmentTree:
    def __init__(self, N):
        self.size = N
        self.tree = [0] * (4 * N)
    
    def update(self, idx, val, node, start, end):
        if idx < start or idx > end:
            return
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        self.update(idx, val, node * 2, start, mid)
        self.update(idx, val, node * 2 + 1, mid + 1, end)
        self.tree[node] = self.tree[node * 2] + self.tree[node * 2 + 1]
    
    def query(self, left, right, node, start, end):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        return self.query(left, right, node * 2, start, mid) + self.query(left, right, node * 2 + 1, mid + 1, end)

def dfs(tree, start_idx, visited, start, end):
    visited[start_idx] = True
    start[start_idx] = end[0]
    for next_idx in tree[start_idx]:
        if not visited[next_idx]:
            end[0] += 1
            dfs(tree, next_idx, visited, start, end)
    end[start_idx] = end[0]

N, M = map(int, input().split())
parents = list(map(int, input().split()))
weights = list(map(int, input().split()))

tree = {i: [] for i in range(1, N + 1)}
for idx, parent in enumerate(parents, 2):
    tree[parent].append(idx)

# 각 노드의 시작과 끝 인덱스를 계산
start, end = {}, [1]
visited = [False] * (N + 1)
dfs(tree, 1, visited, start, end)

segment_tree = SegmentTree(N)
for i in range(1, N + 1):
    segment_tree.update(start[i], weights[i-1], 1, 1, N)

results = []
for _ in range(M):
    query = list(map(int, input().split()))
    if query[0] == 1:
        _, i, j, w = query
        tree[i].append(j + N)
        end[0] += 1
        start[j + N] = end[0]
        end[j + N] = end[0]
        segment_tree.update(start[j + N], w, 1, 1, N)
    else:
        _, i = query
        weight_sum = segment_tree.query(start[i], end[i], 1, 1, N)
        results.append(weight_sum if weight_sum != 0 else -1)

print(results)
