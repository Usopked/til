import sys
sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline

INF = float('inf')

class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.init(arr, 1, 0, self.n-1)
    
    def init(self, arr, node, start, end):
        if start == end:
            self.tree[node] = (arr[start], start)
            return self.tree[node]
        mid = (start + end) // 2
        left = self.init(arr, node*2, start, mid)
        right = self.init(arr, node*2+1, mid+1, end)
        self.tree[node] = min(left, right)
        return self.tree[node]
    
    def update(self, node, start, end, idx, val):
        if idx < start or idx > end:
            return self.tree[node]
        if start == end:
            self.tree[node] = (val, idx)
            return self.tree[node]
        mid = (start + end) // 2
        left = self.update(node*2, start, mid, idx, val)
        right = self.update(node*2+1, mid+1, end, idx, val)
        self.tree[node] = min(left, right)
        return self.tree[node]
    
    def query(self, node, start, end, left, right):
        if right < start or left > end:
            return (INF, INF)
        if left <= start and end <= right:
            return self.tree[node]
        mid = (start + end) // 2
        left_result = self.query(node*2, start, mid, left, right)
        right_result = self.query(node*2+1, mid+1, end, left, right)
        return min(left_result, right_result)

def solve_sequence_queries(N, arr, queries):
    seg_tree = SegmentTree(arr)
    answers = []
    for q in queries:
        if q[0] == 1:
            _, i, v = q
            seg_tree.update(1, 0, N-1, i-1, v)
        else:
            _, i, j = q
            _, idx = seg_tree.query(1, 0, N-1, i-1, j-1)
            answers.append(idx+1)
    return answers

N = int(input())
arr = list(map(int, input().split()))
cnt = int(input())
queries = [tuple(map(int, input().split())) for _ in range(cnt)]
print(*solve_sequence_queries(N, arr, queries), sep='\n')
