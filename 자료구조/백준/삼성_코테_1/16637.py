import sys
input = sys.stdin.readline

def calc(a, b, op):
    if op == '+':
        return a + b
    if op == '-':
        return a - b
    if op == '*':
        return a * b

def solve(idx, res):
    global answer
    if idx > n - 1:
        answer = max(answer, res)
        return
    # 괄호가 없는 경우
    solve(idx + 2, calc(res, int(arr[idx + 1]), arr[idx]))
    # 괄호가 있는 경우
    if idx + 2 < n:
        solve(idx + 4, calc(res, calc(int(arr[idx + 1]), int(arr[idx + 3]), arr[idx + 2]), arr[idx]))

n = int(input().strip())
arr = list(input().strip())
answer = -float('inf')

solve(1, int(arr[0]))

print(answer)
