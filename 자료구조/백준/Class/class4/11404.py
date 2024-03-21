def floyd_warshall(n, buses):
    INF = float('inf')
    
    # 초기화: 2차원 배열을 무한대 값으로 채운다.
    # i에서 j로 가는 경로가 없으면 무한대 값을 가짐
    # i에서 i로 가는 경로의 비용은 0
    distance = [[INF] * n for _ in range(n)]
    for i in range(n):
        distance[i][i] = 0
        
    # 각 버스 노선에 대한 정보를 distance 배열에 추가
    for a, b, c in buses:
        # 시작 도시와 도착 도시를 연결하는 노선이 여러 개일 수 있으므로 최소 비용만 저장
        distance[a-1][b-1] = min(distance[a-1][b-1], c)

    # 플로이드-와샬 알고리즘
    for k in range(n):
        for i in range(n):
            for j in range(n):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # 갈 수 없는 경우는 0으로 변경
    for i in range(n):
        for j in range(n):
            if distance[i][j] == INF:
                distance[i][j] = 0

    return distance

# 예시로 테스트
n = int(input())
num = int(input())
buses = [tuple(map(int,input().split())) for _ in range(num)]
for i in floyd_warshall(n, buses):
    for j in range(n):
        print(i[j], end=' ')
    print('')