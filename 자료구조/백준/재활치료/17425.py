import sys

def sum_of_divisors(max_N):
    divisor_sum = [0] * (max_N + 1)
    for i in range(1, max_N + 1):
        for j in range(i, max_N + 1, i):
            divisor_sum[j] += i
    # 누적합 계산
    for i in range(2, max_N + 1):
        divisor_sum[i] += divisor_sum[i - 1]
    return divisor_sum

max_N = 1000000 
precomputed_sums = sum_of_divisors(max_N)

count = int(sys.stdin.readline())
for _ in range(count):
    N = int(sys.stdin.readline())
    print(precomputed_sums[N])
