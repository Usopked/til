def count_square_free(min_val, max_val):
    is_square_free = [True] * (max_val - min_val + 1)
    
    num = 2
    while num * num <= max_val:
        start = max(num * num, (min_val + num * num - 1) // (num * num) * (num * num))
        for i in range(start, max_val + 1, num * num):
            is_square_free[i - min_val] = False
        num += 1
    return sum(is_square_free)


min_val, max_val = map(int, input().split())
print(count_square_free(min_val, max_val))
