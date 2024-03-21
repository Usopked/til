import sys
input = sys.stdin.readline
class SegmentTree:
    def __init__(self, arr):
        self.N = len(arr)
        self.tree = [0] * (4 * self.N)
        self.init_tree(arr, 1, 0, self.N-1)

    def init_tree(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.tree[node] = self.init_tree(arr, node*2, start, mid) + \
                              self.init_tree(arr, node*2+1, mid+1, end)
        return self.tree[node]

    def update(self, node, start, end, index, diff):
        if index < start or index > end:
            return
        
        self.tree[node] += diff
        
        if start != end:
            mid = (start + end) // 2
            self.update(node*2, start, mid, index, diff)
            self.update(node*2+1, mid+1, end, index, diff)

    def query(self, node, start, end, left, right):
        if left > end or right < start:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        
        mid = (start + end) // 2
        return self.query(node*2, start, mid, left, right) + \
               self.query(node*2+1, mid+1, end, left, right)


def solve_segment_tree_problem(N, M, K, numbers, commands):
    st = SegmentTree(numbers)
    results = []
    
    for cmd in commands:
        if cmd[0] == 1:
            idx, value = cmd[1]-1, cmd[2]
            diff = value - numbers[idx]
            numbers[idx] = value
            st.update(1, 0, N-1, idx, diff)
        else:
            left, right = cmd[1]-1, cmd[2]-1
            results.append(st.query(1, 0, N-1, left, right))
    
    return results

N, M, K = map(int, input().split())
numbers = [int(input()) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M+K)]
results = solve_segment_tree_problem(N, M, K, numbers, commands)
for res in results:
    print(res)