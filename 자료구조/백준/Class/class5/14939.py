import sys
input = sys.stdin.readline

def bulb_switch(state, x, y):
    for dx, dy in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 10 and 0 <= ny < 10:
            state[nx][ny] = 1 - state[nx][ny] 
    return state

def count_switch_presses(initial_state):
    answer = float('inf')
    for switch in range(1024):  # 2^10
        state = [row[:] for row in initial_state] 
        count = 0
        for i in range(10):
            if (switch & (1 << i)) != 0: 
                state = bulb_switch(state, 0, i)
                count += 1
        for i in range(1, 10):
            for j in range(10):
                if state[i-1][j] == 1:
                    state = bulb_switch(state, i, j)
                    count += 1
        if sum(state[-1]) == 0:
            answer = min(answer, count)
    return -1 if answer == float('inf') else answer

input_data = [input() for _ in range(10)]
initial_state = [[1 if ch == 'O' else 0 for ch in line] for line in input_data]
print(count_switch_presses(initial_state))
