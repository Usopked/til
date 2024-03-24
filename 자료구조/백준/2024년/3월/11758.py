points = []
for i in range(3):
    points.append(list(map(int, input().split())))


x1, y1 = points[0]
x2, y2 = points[1]
x3, y3 = points[2]

cross_product = (x2 - x1) * (y3 - y2) - (y2 - y1) * (x3 - x2)

if cross_product > 0:
    direction = 1 
elif cross_product < 0:
    direction = -1
else:
    direction = 0

print(direction)
