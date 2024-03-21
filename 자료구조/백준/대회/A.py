a, b, c = map(int, input().split())
d = a - b*c
if d < 0:
    e = 0
else:
    e = d 
print(e, d+b-1)