import sys
sys.stdin = open(r'C:\Users\ProBook\Desktop\공부파일\자료구조\백준\Class\class6\test.txt', 'r')
input = sys.stdin.readline
class SegmentTree:
    def __init__(self, arr):
        self.arr_size = len(arr)
        self.tree_size = self.arr_size * 4
        self.tree = [0] * self.tree_size
        self.modulo = 1_000_000_007
        self.init_tree(arr, 1, 0, self.arr_size - 1)
        
    def init_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = (self.init_tree(arr, node*2, start, mid) * 
                           self.init_tree(arr, node*2 + 1, mid + 1, end)) % self.modulo
        return self.tree[node]
    
    def update(self, node, start, end, index, value):
        if index < start or index > end:
            return self.tree[node]
        if start == end:
            self.tree[node] = value
            return self.tree[node]
        mid = (start + end) // 2
        self.tree[node] = (self.update(node*2, start, mid, index, value) *
                           self.update(node*2 + 1, mid + 1, end, index, value)) % self.modulo
        return self.tree[node]
    
    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 1
        if left <= start and right >= end:
            return self.tree[node]
        mid = (start + end) // 2
        return (self.query(node*2, start, mid, left, right) *
                self.query(node*2 + 1, mid + 1, end, left, right)) % self.modulo


def solve_problem(N, M, K, arr, operations):
    segment_tree = SegmentTree(arr)
    results = []
    for op in operations:
        if op[0] == 1:
            segment_tree.update(1, 0, N-1, op[1]-1, op[2])
        else:
            results.append(segment_tree.query(1, 0, N-1, op[1]-1, op[2]-1))
    return results

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]
operations = [tuple(map(int, input().split())) for _ in range(M+K)]

print(*solve_problem(N, M, K, arr, operations), sep='\n')
