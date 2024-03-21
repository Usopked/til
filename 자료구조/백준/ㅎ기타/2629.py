from collections import defaultdict

def can_measure(weights, marbles):
    N = len(weights)
    dp = defaultdict(bool)
    dp[0] = True  # base case: no weights can make 0

    for weight in weights:
        temp = dp.copy()  # copy the current dp
        for value, can_make in dp.items():
            if can_make:
                temp[abs(value - weight)] = True
                temp[value + weight] = True
        dp = temp

    return [dp[marble] for marble in marbles]

# test the function
N = input()
weight = list(map(int, input().split()))
M = input()
marble= list(map(int, input().split()))
for i in can_measure(weight, marble):
    if i == True: print('Y', end=' ')
    else: print('N', end=' ')




