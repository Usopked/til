N, L = map(int, input().split())

for length in range(L, 101):  # L부터 100까지 반복
    temp = N - (length * (length - 1) // 2)  # 연속된 수의 합 공식을 이용하여 temp(x * length) 계산
    if temp % length == 0:  # temp가 length로 나누어떨어지는 경우
        x = temp // length  # 시작점 x 계산
        if x >= 0:  # x가 음이 아닌 정수인 경우
            for i in range(length):  # 연속된 수 출력
                print(x + i, end=' ')
            break
else:  # for-else 구문을 사용하여, 반복문이 break 없이 종료된 경우 -1 출력
    print(-1)
