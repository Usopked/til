from itertools import combinations

def can_reduce_to_one(N, B):
    # B에 있는 수들을 제외한 나머지 수를 A에 넣는다.
    A = set(range(1, N+1)) - set(B)
    
    while len(A) > 1:
        # 연산을 한 번도 수행하지 못한 경우 반복문 종료
        performed = False
        
        # 연산을 수행할 수 있는지 확인
        for x in list(A):
            y1, y2, z = x+1, x+2, x+3
            if y1 in A and y2 in B:
                A.remove(x)
                A.remove(y1)
                B.remove(y2)
                A.add(z)
                performed = True
                break
            
            if y1 in B and y2 in A:
                A.remove(y2)
                B.remove(y1)
                A.add(x)
                performed = True
                break
        
        # 한 번도 연산을 수행하지 못한 경우
        if not performed:
            return False

    # A의 원소가 1개로 줄어들면 True 반환
    return len(A) == 1

def solve(N, M):
    # 가능한 모든 B의 조합을 생성
    all_cases = list(combinations(range(1, N+1), M))
    
    for B in all_cases:
        # 연속된 수가 있는지 확인
        is_continuous = any((B[i] + 1 == B[i+1]) for i in range(len(B)-1))
        if is_continuous:
            continue
        
        # 조합 B에 대해 A의 원소를 1개로 줄일 수 있는지 확인
        if can_reduce_to_one(N, list(B)):
            return M, B
    
    return -1, []

# 입력 예제
N, M = 6, 1
print(solve(N, M))
