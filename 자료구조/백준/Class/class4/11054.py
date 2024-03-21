def longest_bitonic_sequence(arr):
    N = len(arr)
    
    # Step 1: LIS from left
    lis_left = [1] * N
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                lis_left[i] = max(lis_left[i], lis_left[j] + 1)
    
    # Step 2: LDS from right
    lds_right = [1] * N
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, i, -1):
            if arr[i] > arr[j]:
                lds_right[i] = max(lds_right[i], lds_right[j] + 1)
    
    # Step 3: Calculate result
    max_length = 0
    for i in range(N):
        max_length = max(max_length, lis_left[i] + lds_right[i] - 1)
    
    return max_length

# Test case
buf = input()
arr = list(map(int, input().split()))
print(longest_bitonic_sequence(arr))
