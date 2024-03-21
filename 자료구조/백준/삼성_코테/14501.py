#동적 프로그래밍(Dynamic Programming), 가중치
#계단 오르기 문제: 한 번에 두 칸까지 계단을 오를 수 있다고 가정하면, N까지의 계단을 오르는 모든 경우의 수는 (N-1) + (N-2)이다
#여기서는 N에 따른 가중치를 비교하여 더 큰 것을 선택함(if문)


def max_weight(N, arr):
    dp = [0] * (N+1)
    max_val = 0
    for i in range(N-1, -1, -1):
        time = arr[i][0]
        pay = arr[i][1]
        if time + i <= N:
            dp[i] = max(pay + dp[i+time], max_val)
            max_val = dp[i]
        else:
            dp[i] = max_val
    return max_val

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append((a, b))

print(max_weight(N, arr))
