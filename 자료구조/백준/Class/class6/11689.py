def euler_phi(n):
    result = n  
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        result -= result // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n //= i
            result -= result // i
        i += 2
        
    if n > 1:
        result -= result // n
        
    return result

n = int(input())
print(euler_phi(n))
