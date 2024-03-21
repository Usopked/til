N = int(input())
arr = list(map(int, input().split()))
B, C = map(int, input().split())

total = 0
for i in range(N):
    arr[i] -= B
    total += 1
    if arr[i] > 0:
        total += (arr[i] - 1) // C + 1  # ceil 구현을 위한 조건

print(total)
