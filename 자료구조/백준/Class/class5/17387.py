import sys
input = sys.stdin.readline

def ccw(x1, y1, x2, y2, x3, y3):
    value = (x2 - x1) * (y3 - y1) - (y2 - y1) * (x3 - x1)
    if value > 0:   
        return 1
    elif value < 0:  
        return -1
    else:  
        return 0

def is_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    ab_ccw = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cd_ccw = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    
    if ab_ccw == 0 and cd_ccw == 0: 
        if (min(x1, x2) <= max(x3, x4) and max(x1, x2) >= min(x3, x4) and
            min(y1, y2) <= max(y3, y4) and max(y1, y2) >= min(y3, y4)):
            return 1
        return 0
    return 1 if ab_ccw <= 0 and cd_ccw <= 0 else 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(is_intersect(x1, y1, x2, y2, x3, y3, x4, y4))
