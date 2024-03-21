def min_time_to_solve(N, problems_to_solve, problems):
    problems_by_difficulty = [[] for _ in range(5)]
    for k, t in problems:
        problems_by_difficulty[k-1].append(t)
    for i in range(5):
        problems_by_difficulty[i].sort()
    total_time = 0
    for i in range(5):
        for j in range(problems_to_solve[i]):
            total_time += problems_by_difficulty[i][j]
            if j == 0 and i > 0:
                total_time += 60
            elif j > 0:
                total_time += problems_by_difficulty[i][j] - problems_by_difficulty[i][j-1]
    
    return total_time
N = int(input().strip())
problems_to_solve = list(map(int, input().strip().split()))
problems = [tuple(map(int, input().strip().split())) for _ in range(N)]

print(min_time_to_solve(N, problems_to_solve, problems))

