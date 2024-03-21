import heapq
import sys
input = sys.stdin.readline

def max_steal_value(N, K, jewels, bags):
    jewels.sort(key=lambda x: x[0])
    bags.sort()
    value = 0
    available_jewels = []
    j_idx = 0
    for bag in bags:
        while j_idx < N and jewels[j_idx][0] <= bag:
            heapq.heappush(available_jewels, -jewels[j_idx][1])
            j_idx += 1
        if available_jewels:
            value -= heapq.heappop(available_jewels)

    return value

N, K = map(int, input().split())
jewels = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

print(max_steal_value(N, K, jewels, bags))
