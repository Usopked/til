from collections import Counter

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

def operate(A):
    max_length = 0
    for i in range(len(A)):
        cnt = Counter(A[i])
        if cnt[0]:
            del cnt[0]
        A[i] = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        max_length = max(max_length, len(A[i]))
    for i in range(len(A)):
        A[i] = [item for sublist in A[i] for item in sublist] + [0] * (max_length * 2 - len(A[i]) * 2)
        A[i] = A[i][:100]
    return A

for time in range(101):
    if r - 1 < len(A) and c - 1 < len(A[0]) and A[r - 1][c - 1] == k:
        print(time)
        break
    if len(A) >= len(A[0]):
        A = operate(A)
    else:
        A = list(map(list, zip(*A)))
        A = operate(A)
        A = list(map(list, zip(*A)))
else:
    print(-1)
