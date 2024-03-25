#신발끈 공식(다각형 꼭짓점 좌표로 면적 계산, 벡터 외적 응용)
import sys
cnt = int(sys.stdin.readline())
points = []
for i in range(cnt):
    points.append(tuple(map(int, sys.stdin.readline().split())))

sum1 = sum(points[i][0] * points[(i + 1) % len(points)][1] for i in range(len(points)))
sum2 = sum(points[i][1] * points[(i + 1) % len(points)][0] for i in range(len(points)))

area = abs(sum1 - sum2) / 2
print(area)