from itertools import combinations

# 입력 받기
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]

# 치킨집과 집의 좌표 찾기
chickens, houses = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 2:
            chickens.append((i, j))
        elif city[i][j] == 1:
            houses.append((i, j))

# 치킨집 M개를 선택하는 모든 조합을 찾기
comb = list(combinations(chickens, M))

# 도시의 치킨 거리의 최소값 찾기
min_distance = float('inf')
for chicken in comb:
    distance = 0
    for house in houses:
        distance += min([abs(house[0] - i[0]) + abs(house[1] - i[1]) for i in chicken])
    min_distance = min(min_distance, distance)

print(min_distance)
