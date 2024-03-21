def draw_star(n):
    if n == 3:
        return ['  *  ', ' * * ', '*****']
    
    k = n // 2
    prev_star = draw_star(k)
    
    top = [' ' * k + line + ' ' * k for line in prev_star]
    middle = [line + ' ' + line for line in prev_star]
    
    return top + middle

def print_star(n):
    # 별을 그리기 위한 준비
    star_lines = draw_star(n)
    # 별 그리기
    for line in star_lines:
        print(line)

n = int(input()) 
print_star(n)

