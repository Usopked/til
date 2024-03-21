#DPS(깊이 우선 탐색)

n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 1e9
max_value = -1e9

def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + numbers[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - numbers[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * numbers[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / numbers[i]))  # 음수를 양수로 나눌 때는 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼다.
            div += 1

dfs(1, numbers[0])

print(max_value)
print(min_value)
