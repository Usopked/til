#deque가 아닌 heapq로 구현
import heapq

def solve_problem_order_optimized(N, relations):
    indegree = [0] * (N + 1)
    graph = [[] for _ in range(N + 1)]
    
    for a, b in relations:
        graph[a].append(b)
        indegree[b] += 1

    result = []
    pq = []

    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(pq, i)

    while pq:
        now = heapq.heappop(pq)
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1
            
            if indegree[i] == 0:
                heapq.heappush(pq, i)

    return result

# 예제 입력
N, M = map(int, input().split())
relations = [tuple(map(int, input().split())) for _ in range(M)]

for i in solve_problem_order_optimized(N, relations):
    print(i, end=' ')