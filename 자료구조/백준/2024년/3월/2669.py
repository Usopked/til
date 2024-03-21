

arr = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    a, b, x, y = map(int, input().split())
    for i in range(a, x):
        for j in range(b, y):
            arr[i][j] = 1

print(sum(sum(row) for row in arr))
         