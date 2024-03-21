import sys
input = sys.stdin.readline
from bisect import bisect_left
def lis(a):
    values = []
    
    for val in a:
        if not values or val > values[-1]:
            values.append(val)
        else:
            p = bisect_left(values, val)
            values[p] = val
    
    return len(values)


cnt = int(input())
a = list(map(int, input().split()))
print(lis(a))
