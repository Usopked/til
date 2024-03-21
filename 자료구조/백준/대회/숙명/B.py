import sys
input = sys.stdin.readline

def cnt(N, M, K, seat):
    count = 0
    for i in range(N):
        con = 0
        pos = 0
        for j in range(M):
            if seat[i][j] == '0':
                con += 1
                if con == K:
                    pos += 1
                    con -= 1
            else:
                con = 0
        count += pos
    
    return count
N, M, K = map(int, input().split())
seat = [input() for _ in range(N)]

print(cnt(N, M, K, seat))
