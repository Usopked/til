import sys
input = sys.stdin.readline
def max_commuters(n, locations, d):
    points = []
    
    for i, (h, o) in enumerate(locations):
        points.append((h, i, 'H'))
        points.append((o, i, 'O'))

    points.sort(key=lambda x: x[0])

    max_count = 0
    i, j = 0, 0
    homes = set()
    offices = set()
    counter = 0  # To count number of people whose both home and office are within range

    while i < len(points) and j < len(points):
        while j < len(points) and points[j][0] - points[i][0] <= d:
            if points[j][2] == 'H':
                homes.add(points[j][1])
                if points[j][1] in offices:
                    counter += 1
            else:
                offices.add(points[j][1])
                if points[j][1] in homes:
                    counter += 1
            j += 1

        max_count = max(max_count, counter)

        if points[i][2] == 'H':
            homes.remove(points[i][1])
            if points[i][1] in offices:
                counter -= 1
        else:
            offices.remove(points[i][1])
            if points[i][1] in homes:
                counter -= 1
        i += 1

    return max_count
cnt = int(input())
sample_input = [tuple(map(int, input().split())) for _ in range(cnt)]
cct = int(input())
print(max_commuters(cnt, sample_input, cct))
