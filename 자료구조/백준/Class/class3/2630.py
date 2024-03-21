N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0

def cut(x, y, n):
    global white, blue  # 이전에 계산된 결과값을 가져옴
    check = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if check != paper[i][j]:  # 한 번이라도 다른 값이 나오면
                cut(x, y, n//2)  # 2등분해서 재귀
                cut(x, y+n//2, n//2)
                cut(x+n//2, y, n//2)
                cut(x+n//2, y+n//2, n//2)
                return

    if check == 0:  # 위의 반복문을 무사히 통과했다면 모든 값이 같다는 것임
        white += 1  # 모두 흰색이었다면 white 증가
    else:
        blue += 1  # 모두 파란색이었다면 blue 증가

cut(0, 0, N)
print(white)
print(blue)
