
n = int(input())
m = int(input())
n_inputs = [input() for _ in range(m)]
relationships = []
for i in range(len(n_inputs)):
    # 입력 문자열을 공백으로 분할
    input_list = n_inputs[i].split()

    # 튜플의 첫 번째 요소를 문자열로, 그 이후의 요소를 정수로 변환
    tuple_input = (input_list[0],) + tuple(map(int, input_list[1:]))

    # 결과 리스트에 추가
    relationships.append(tuple_input)

    # Union-Find 자료구조를 위한 초기화

# 각 학생이 속한 팀을 저장하는 리스트
team = [i for i in range(n+1)]

# 각 학생의 부모 노드를 저장하는 리스트 (자기 자신으로 초기화)
parent = [i for i in range(n+1)]

# 각 학생의 원수를 저장하는 리스트
enemies = [0 for _ in range(n+1)]

# find 함수: x가 속한 팀의 대표를 찾는 함수
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # 경로 압축
    return parent[x]

# union 함수: x가 속한 팀과 y가 속한 팀을 합치는 함수
def union(x, y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return

    # 더 작은 팀을 더 큰 팀에 합침
    if x < y:
        x, y = y, x
    parent[y] = x

# 학생 간의 관계를 그래프에 추가하고, 동시에 Union-find 자료구조를 업데이트
for relationship in relationships:
    r, a, b = relationship
    if r == "F":  # 친구 관계
        union(a, b)
    else:  # 원수 관계
        if enemies[a] == 0:
            enemies[a] = b
        else:
            union(enemies[a], b)
        if enemies[b] == 0:
            enemies[b] = a
        else:
            union(enemies[b], a)

# 각 학생이 속한 팀을 결정
for i in range(1, n+1):
    find(i)

# 생성된 팀의 개수를 세어 출력
team_count = len(set(parent)) - 1  # 팀 번호 0은 사용하지 않았으므로 제외

print(team_count)
