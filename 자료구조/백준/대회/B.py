import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a*b) // gcd(a,b)

def ftime(N, M):

    cycle_A = 2 * (N-1)
    cycle_B = M
    combined_cycle = lcm(cycle_A, cycle_B)
    for t in range(1, combined_cycle + 1):
        pos_A = N - (t % cycle_A) if t % cycle_A < N else t % cycle_A
        pos_B = (t % cycle_B) if t % cycle_B != 0 else cycle_B
        if pos_A == pos_B:
            return t
        if t >= N * M:
            return -1
    return -1

T = int(input())
arr = [list(map(int, input().split())) for _ in range(T)]
ans = [0]*T
for i in range(T):
    ans[i] = (ftime(arr[i][0], arr[i][1]))
    
print(*ans, sep='\n')