'''인구 이동
1. N*N크기의 배열이 있고, 배열의 각 칸에는 임의의 가중치가 배정됨.
2. 배열의 각 칸마다 해당 칸의 가중치를 담은 노드를 생성함.
3. 배열 상에서 서로 붙어있는 두 칸의 수 차이가 L~R 사이인 모든 칸의 노드를 연결.
4. 연결된 모든 노드의 가중치를 (연결된 노드가 가진 모든 가중치의 합//연결된 노드의 수)로 재할당한 후, 모든 연결을 끊음.
5. 더 이상 노드가 연결되지 않을 때까지 2~4번을 반복한 후, 반복의 총 횟수를 출력함.'''

'''
bfs 함수
solution 함수
먼저 bfs 함수부터 살펴봅시다. 이 함수는 주어진 위치 (i, j)에서 시작하여 BFS(Breadth-First Search)를 수행합니다. 이때, BFS는 배열의 각 칸에서 시작하여 상하좌우로 연결된 칸을 방문하는 방식으로 수행됩니다. 연결 조건은 두 칸의 가중치 차이가 L 이상 R 이하인 경우입니다. 이를 만족하는 모든 칸을 방문하며, 연결된 칸들의 가중치 총합과 칸의 수를 구합니다. 그 후, 각 칸의 가중치를 (연결된 칸들의 가중치 총합 // 연결된 칸의 수)로 업데이트합니다.

다음으로 solution 함수를 살펴봅시다. 이 함수는 주어진 배열에 대해 다음의 과정을 반복합니다:

union 배열을 초기화하고, 모든 칸에 대해 bfs 함수를 수행합니다. 이때, union 배열은 각 칸이 어떤 칸과 연결되어 있는지를 나타냅니다. 초기에는 모든 칸이 연결되지 않은 상태(-1)로 설정됩니다.
bfs 함수를 수행하면서 union 배열을 업데이트하고, 각 칸의 가중치를 업데이트합니다.
모든 칸에 대해 bfs 함수를 수행한 후, 모든 칸이 연결되지 않은 상태라면 반복을 종료합니다.
이 과정이 반복되는 횟수를 반환합니다.'''

from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j, idx, union, arr):
    q = deque()
    q.append((i, j))

    union[i][j] = idx
    summary = arr[i][j]
    count = 1
    united = []
    united.append((i, j))

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N and union[nx][ny] == -1:
                if L <= abs(arr[x][y] - arr[nx][ny]) <= R:
                    q.append((nx, ny))
                    union[nx][ny] = idx
                    summary += arr[nx][ny]
                    count += 1
                    united.append((nx, ny))
    for i, j in united:
        arr[i][j] = summary // count
    return count

def solution(N, L, R, arr):
    total_count = 0
    while True:
        union = [[-1]*N for _ in range(N)]
        idx = 0
        for i in range(N):
            for j in range(N):
                if union[i][j] == -1:
                    bfs(i, j, idx, union, arr)
                    idx += 1
        if idx == N*N:
            break
        total_count += 1
    return total_count

# Test the function
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, L, R, arr))  # It should return 1
