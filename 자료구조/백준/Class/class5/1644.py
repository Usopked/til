def eratosthenes(N):
    sieve = [True] * (N + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(N**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, N + 1, i):
                sieve[j] = False
    return [i for i in range(2, N + 1) if sieve[i]]

def count_consecutive_prime_sums(N):
    primes = eratosthenes(N)
    start, end = 0, 0
    current_sum = 0
    count = 0
    
    while True:
        if current_sum >= N:
            current_sum -= primes[start]
            start += 1
        elif end == len(primes):
            break
        else:
            current_sum += primes[end]
            end += 1
        
        if current_sum == N:
            count += 1
            
    return count

N = int(input())
print(count_consecutive_prime_sums(N))
