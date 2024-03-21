from collections import deque
from itertools import product

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def solution(N, M, K, A, trees):
    # Initialize nutrients map and trees map
    nutrients = [[5]*N for _ in range(N)]
    trees_map = [[deque() for _ in range(N)] for _ in range(N)]

    # Place the trees
    for x, y, z in trees:
        trees_map[x-1][y-1].append(z)

    # Sort the trees by age
    for i in range(N):
        for j in range(N):
            trees_map[i][j] = deque(sorted(trees_map[i][j]))

    # Loop for K years
    for _ in range(K):
        # Spring & Summer
        for i, j in product(range(N), repeat=2):
            len_tree = len(trees_map[i][j])
            for k in range(len_tree):
                if trees_map[i][j][k] <= nutrients[i][j]:
                    nutrients[i][j] -= trees_map[i][j][k]
                    trees_map[i][j][k] += 1
                else:
                    while len_tree > k:
                        nutrients[i][j] += trees_map[i][j].pop() // 2
                        len_tree -= 1
                    break

        # Autumn
        for i, j in product(range(N), repeat=2):
            for age in trees_map[i][j]:
                if age % 5 == 0:
                    for dir in range(8):
                        nx, ny = i + dx[dir], j + dy[dir]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees_map[nx][ny].appendleft(1)

        # Winter
        for i, j in product(range(N), repeat=2):
            nutrients[i][j] += A[i][j]

    # Count the number of trees
    num_trees = 0
    for i in range(N):
        for j in range(N):
            num_trees += len(trees_map[i][j])

    return num_trees

# Test the function
N, M, K = map(int,(input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
trees = [deque(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, A, trees))  # It should return 85
