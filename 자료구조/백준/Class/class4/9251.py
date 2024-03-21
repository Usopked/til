def lcs_length(str1, str2):
    # DP 테이블 초기화
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

    # DP를 이용하여 LCS 길이 계산
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[len(str1)][len(str2)]

# 예제 입력
str1 = input()
str2 = input()

print(lcs_length(str1, str2))
