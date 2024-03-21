from itertools import permutations

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
orders = list(permutations([2,3,4,5,6,7,8,9], 8)) # 순열 리스트 생성
max_score = 0

for order in orders:
    order = list(order)
    order.insert(3, 1) # 1번 선수는 4번타자
    idx, score = 0, 0
    for i in range(N):
        out, b1, b2, b3 = 0, 0, 0, 0
        while out < 3:
            if A[i][order[idx%9]-1] == 0: 
                out += 1
            elif A[i][order[idx%9]-1] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif A[i][order[idx%9]-1] == 2:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif A[i][order[idx%9]-1] == 3:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif A[i][order[idx%9]-1] == 4:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            idx += 1
    max_score = max(max_score, score)

print(max_score)
