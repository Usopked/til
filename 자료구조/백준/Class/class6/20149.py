def ccw(a, b, c):
    op = a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - (a[1]*b[0] + b[1]*c[0] + c[1]*a[0])
    return 1 if op > 0 else (-1 if op < 0 else 0)

def is_intersect(s1, s2):
    a, b = s1
    c, d = s2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    return not (ab > 0 or cd > 0) and (ab >= 0 and cd >= 0)

def intersection_point(s1, s2):
    x1, y1 = s1[0]
    x2, y2 = s1[1]
    x3, y3 = s2[0]
    x4, y4 = s2[1]
    
    det = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if det == 0:
        return None

    px = ((x1*y2 - y1*x2) * (x3 - x4) - (x1 - x2) * (x3*y4 - y3*x4)) / det
    py = ((x1*y2 - y1*x2) * (y3 - y4) - (y1 - y2) * (x3*y4 - y3*x4)) / det

    return px, py

def format_output(val):
    return format(val, '.10f').rstrip('0').rstrip('.')
def check_intersection(s1, s2):
    a, b = s1
    c, d = s2
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)

    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return not (b < c or d < a)
    return ab <= 0 and cd <= 0

def main():
    l1 = tuple(map(int, input().split()))
    l2 = tuple(map(int, input().split()))

    s1 = ((l1[0], l1[1]), (l1[2], l1[3]))
    s2 = ((l2[0], l2[1]), (l2[2], l2[3]))

    if check_intersection(s1, s2):
        print(1)
        point = intersection_point(s1, s2)
        if point:
            print(f"{format_output(point[0])} {format_output(point[1])}")
    else:
        print(0)
main()