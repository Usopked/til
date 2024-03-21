import sys
sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(float('inf'), -float('inf'))] * (4 * self.n)  # (min, max)
        self.init_tree(arr, 1, 0, self.n - 1)

    def init_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], arr[start])
            return self.tree[node]
        
        mid = (start + end) // 2
        left_min, left_max = self.init_tree(arr, node * 2, start, mid)
        right_min, right_max = self.init_tree(arr, node * 2 + 1, mid + 1, end)
        
        self.tree[node] = (min(left_min, right_min), max(left_max, right_max))
        return self.tree[node]

    def query(self, node, start, end, left, right):
        # If the current segment is disjoint with the query segment
        if left > end or right < start:
            return float('inf'), -float('inf')
        
        # If the current segment is entirely inside the query segment
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        left_min, left_max = self.query(node * 2, start, mid, left, right)
        right_min, right_max = self.query(node * 2 + 1, mid + 1, end, left, right)
        
        return min(left_min, right_min), max(left_max, right_max)

def solve_segment_tree(N, M, nums, queries):
    segment_tree = SegmentTree(nums)
    results = []
    for a, b in queries:
        min_val, max_val = segment_tree.query(1, 0, N - 1, a - 1, b - 1)
        results.append((min_val, max_val))
    return results

# Sample Test
N, M = map(int, input().split())
nums = [int(input()) for _ in range(N)]
queries =  [tuple(map(int, input().split())) for _ in range(M)]
for li in solve_segment_tree(N, M, nums, queries):
    print(*li)