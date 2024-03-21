from itertools import combinations

def count_subsets(n, s, arr):
    # Split the list into two halves
    half_size = n // 2
    left = arr[:half_size]
    right = arr[half_size:]

    # Calculate all possible sums for the left half
    left_sums = []
    for i in range(1, len(left) + 1):
        for combination in combinations(left, i):
            left_sums.append(sum(combination))

    # Calculate all possible sums for the right half
    right_sums = []
    for i in range(1, len(right) + 1):
        for combination in combinations(right, i):
            right_sums.append(sum(combination))

    # Count how many pairs of sums from left and right make the desired sum
    count = 0
    for ls in left_sums:
        if s - ls in right_sums:
            count += right_sums.count(s - ls)

    # Additionally, check if there are subsets with sum s in each half
    count += left_sums.count(s)
    count += right_sums.count(s)

    return count

n, s = map(int, input().split())
arr = list(map(int, input().split()))
print(count_subsets(n, s, arr))
