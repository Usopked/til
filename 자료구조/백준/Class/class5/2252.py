from collections import deque

def topological_sort(N, comparisons):
    # 각 정점의 진입 차수를 저장하는 리스트
    indegree = [0] * (N + 1)
    
    # 그래프 초기화
    graph = [[] for _ in range(N + 1)]
    
    # 그래프 및 진입 차수 정보 생성
    for a, b in comparisons:
        graph[a].append(b)
        indegree[b] += 1

    # 위상 정렬 수행
    result = []
    q = deque()

    # 초기에 진입 차수가 0인 노드를 큐에 삽입
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        now = q.popleft()
        result.append(now)

        # 해당 노드와 연결된 노드들의 진입 차수 감소
        for i in graph[now]:
            indegree[i] -= 1
            
            # 새롭게 진입 차수가 0이 된 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    return result

# 예제 입력
N, M = map(int, input().split())
comparisons = [tuple(map(int, input().split())) for _ in range(M)]

for i in topological_sort(N, comparisons):
    print(i, end=' ')
