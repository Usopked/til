N = int(input())
buildings = list(map(int, input().split()))
visible_count = [0]*N

for i in range(N):
    for j in range(i+1, N):
        cnt = 0
        for k in range(i+1, j):
            if buildings[k] < buildings[i] + (buildings[j]-buildings[i])*(k-i)/(j-i):
                cnt += 1
        if cnt == j-i-1:
            visible_count[i] += 1
            visible_count[j] += 1

print(max(visible_count))
