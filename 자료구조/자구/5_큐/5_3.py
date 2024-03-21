def solution(n):
    q = [1]
    answer, i, total = 1, 1, 1
    mid = (n + 1) // 2
    while i < mid:
        i += 1
        total += i
        q.append(i)
        while total > n:
            total -= q.pop(0)
        if total == n:
            answer += 1
    return answer

print(solution(15))