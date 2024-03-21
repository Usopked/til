def count_digits(N):
    result = [0] * 10
    factor = 1
    
    while N // factor > 0:
        low = N - (N // factor) * factor
        curr = (N // factor) % 10
        high = N // (factor * 10)
        
        for i in range(1, 10):
            if i < curr:
                result[i] += (high + 1) * factor
            elif i == curr:
                result[i] += high * factor + low + 1
            else:
                result[i] += high * factor
        if curr == 0:
            result[0] += high * factor - factor + low + 1
        else:
            result[0] += high * factor
        factor *= 10

    return result


print(*count_digits(int(input())))
