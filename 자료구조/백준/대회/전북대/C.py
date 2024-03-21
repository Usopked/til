from math import gcd
from functools import reduce

def lcm(x, y):
    return x * y // gcd(x, y)

def min_voters(v):
    def gcd_list(nums):
        return reduce(gcd, nums)
    total = sum(v)
    g = gcd_list(v)
    return total // g

def calculate(v1, v2, min1):
    factor = 1
    while True:
        max_required = 0  # 각 항목별 필요한 최소 투표 수 중 최대값

        for i in range(len(v1)):
            required_vote = v1[i] * factor
            max_required = max(max_required, (required_vote + v2[i] - 1) // v2[i])

        total_votes = sum(max_required * v2[i] for i in range(len(v2)))

        if total_votes <= min1 * factor:
            return total_votes

        factor += 1

N, P = map(int, input().split())
multiplier = 10 ** P if P else 1

v1 = [int(x) for x in input().split()]
v2 = [int(x) for x in input().split()]

min1 = min_voters(v1)
min2 = calculate(v1, v2, min1)

print(min1, min2)


