import sys
input = sys.stdin.readline

def ccw(A, B, C):
    return (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0])

def is_intsct(A, B, C, D):
    if (ccw(A, B, C) * ccw(A, B, D) <= 0) and (ccw(C, D, A) * ccw(C, D, B) <= 0):
        if (min(A[0], B[0]) <= max(C[0], D[0]) and max(A[0], B[0]) >= min(C[0], D[0]) and
            min(A[1], B[1]) <= max(C[1], D[1]) and max(A[1], B[1]) >= min(C[1], D[1])):
            return True
        return ccw(A, B, C) * ccw(A, B, D) != 0 and ccw(C, D, A) * ccw(C, D, B) != 0
    return False

class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.r = [0] * n
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            if self.r[rx] > self.r[ry]:
                rx, ry = ry, rx
            self.p[rx] = ry
            if self.r[rx] == self.r[ry]:
                self.r[ry] += 1
            self.s[ry] += self.s[rx]

    def size(self, x):
        return self.s[self.find(x)]

def seg_group(segs):
    n = len(segs)
    uf = UF(n)

    for i in range(n):
        for j in range(i+1, n):
            if is_intsct(segs[i][0], segs[i][1], segs[j][0], segs[j][1]):
                uf.union(i, j)

    gc = len(set(uf.find(i) for i in range(n)))
    gs = max(uf.size(i) for i in range(n))

    return gc, gs

def find_groups(n, inp_segs):
    segs = [((x1, y1), (x2, y2)) for x1, y1, x2, y2 in inp_segs]
    print(seg_group(segs)[0])
    print(seg_group(segs)[1])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

find_groups(n, arr)