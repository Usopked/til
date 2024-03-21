'''def is_valid(queen_positions, next_queen_row, next_queen_col):
    for current_row in range(next_queen_row):
        # 같은 열에 위치하는지 검사
        if queen_positions[current_row] == next_queen_col:
            return False
        # 대각선 상에 위치하는지 검사
        if queen_positions[current_row] - current_row == next_queen_col - next_queen_row:
            return False
        if queen_positions[current_row] + current_row == next_queen_col + next_queen_row:
            return False
    return True

def n_queens(n, row=0, queen_positions=[]):
    if row == n:
        return 1
    count = 0
    for col in range(n):
        if is_valid(queen_positions, row, col):
            count += n_queens(n, row + 1, queen_positions + [col])
    return count

print(n_queens(int(input())))'''

def n_queen_python(n):
    left = [0] * 30
    right = [0] * 30
    row = [0] * 30
    cnt = 0

    def f(in_):
        nonlocal cnt
        if in_ == n+1:
            cnt += 1
            return
        for i in range(1, n+1):
            if row[i] == 0 and left[in_+i] == 0 and right[n+in_-i] == 0:
                row[i] = 1
                left[in_+i] = 1
                right[n+in_-i] = 1
                f(in_+1)
                row[i] = 0
                left[in_+i] = 0
                right[n+in_-i] = 0

    f(1)
    return cnt

print(n_queen_python(int(input())))
