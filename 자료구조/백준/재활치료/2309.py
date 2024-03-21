from itertools import combinations as cb
dw = []
for _ in range(9):
    dw.append(int(input()))

for i in cb(dw, 2):
    if sum(i) == sum(dw)-100:
        dw.remove(i[0])
        dw.remove(i[1])
dw.sort()
for i in range(len(dw)):
    print(dw[i])