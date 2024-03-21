N, M = map(int, input().split())
paper = [list(map(int, list(input().strip()))) for _ in range(N)]
ans = 0
for s in range(1 << N * M):
    sum = 0
    for i in range(N):
        cur = 0
        for j in range(M):
            k = i * M + j
            if (s & (1 << k)) > 0:  # If the k-th bit of s is 1
                cur = cur * 10 + paper[i][j]
            else:  # If the k-th bit of s is 0 or it's the end of the line
                sum += cur
                cur = 0
        sum += cur
    for j in range(M):
        cur = 0
        for i in range(N):
            k = i * M + j
            if (s & (1 << k)) == 0:  # If the k-th bit of s is 0
                cur = cur * 10 + paper[i][j]
            else:  # If the k-th bit of s is 1 or it's the end of the column
                sum += cur
                cur = 0
        sum += cur
    ans = max(ans, sum)
print(ans)
