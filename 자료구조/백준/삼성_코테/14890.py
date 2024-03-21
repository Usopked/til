import sys

def check(li):
    global L
    visit = [False] * len(li)
    for i in range(len(li) - 1):
        if abs(li[i] - li[i+1]) > 1:
            return False
        if li[i] < li[i+1]:  
            temp = li[i]
            for j in range(i, i - L, -1):
                if j < 0 or li[j] != temp or visit[j] == True:
                    return False
                visit[j] = True
        elif li[i] > li[i+1]:  
            temp = li[i+1]
            for j in range(i+1, i + L + 1):
                if j >= N or li[j] != temp or visit[j] == True:
                    return False
                visit[j] = True
    return True

N, L = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
count = 0

for i in board:
    if check(i):
        count += 1
for i in list(zip(*board)):  
    if check(i):
        count += 1

print(count)
