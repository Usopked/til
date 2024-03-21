import sys
input = sys.stdin.readline

from bisect import bisect_left
def lis(a):
    L = []
    values = []
    prev = [-1] * len(a)
    
    for i, val in enumerate(a):
        if not values or val > values[-1]:
            if values:
                prev[i] = L[-1]
            values.append(val)
            L.append(i)
        else:
            p = bisect_left(values, val)
            values[p] = val
            if p > 0:
                prev[i] = L[p-1]
            L[p] = i
    
    res = []
    i = L[-1]
    while i != -1:
        res.append(a[i])
        i = prev[i]
    
    return len(res), res[::-1]


cnt = int(input())
a = list(map(int, input().split()))
print(lis(a)[0])
print(*lis(a)[1])
