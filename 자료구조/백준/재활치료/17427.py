def sum_of_divisors(N):
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        for j in range(i, N + 1, i):
            result[j] += i
    return result

N = int(input())
cnt = 0
divisor_sums = sum_of_divisors(N)
for i in range(1, N + 1):
    cnt += divisor_sums[i]
print(cnt)
        
    