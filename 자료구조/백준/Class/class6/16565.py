from math import comb

def winning_cases(N):
    result = 0
    for k in range(1, min(13, N//4) + 1):
        current_cases = comb(13, k) * comb(52 - 4*k, N - 4*k)
        
        if k % 2 == 1:
            result += current_cases
        else:
            result -= current_cases
        
        result %= 10007
    
    return result

test_cases = int(input())
print(winning_cases(test_cases))
