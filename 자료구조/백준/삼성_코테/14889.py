from itertools import combinations
import sys
#조합과 브루트 포스 사용

# 배열의 크기 N 입력 받기
N = int(input())

# 배열 S 초기화
S = [list(map(int, input().split())) for _ in range(N)]

members = [i for i in range(N)]
possible_team = []

# 조합을 이용하여 가능한 팀 생성하기
for team in list(combinations(members, N // 2)):
    possible_team.append(team)

min_val = sys.maxsize
for i in range(len(possible_team) // 2):
    # 스타트 팀
    team = possible_team[i]
    start_val = 0 # 스타트 팀의 가중치 합
    for j in range(N//2):
        member = team[j] # 팀 멤버
        for k in team:
            start_val += S[member][k] + S[k][member] # 가중치 합산

    # 링크 팀
    team = possible_team[-i-1]
    link_val = 0 # 링크 팀의 가중치 합
    for j in range(N//2):
        member = team[j] # 팀 멤버
        for k in team:
            link_val += S[member][k] + S[k][member] # 가중치 합산

    min_val = min(min_val, abs(start_val - link_val)) # 가중치 차이의 최솟값 갱신

print(min_val) # 결과 출력
